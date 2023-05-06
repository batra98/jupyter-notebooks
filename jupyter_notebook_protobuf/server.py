from jupyter_notebook_protobuf.config import (
    DATABASE_URL,
    REDIS_PORT,
    REDIS_HOST,
)

from jupyter_notebook_protobuf.protoc.gen.notebook_pb2_grpc import (
    NotebookServiceServicer,
    add_NotebookServiceServicer_to_server,
)
from jupyter_notebook_protobuf.protoc.gen.notebook_pb2 import (
    Notebook,
    NotebookCreateRequest,
    NotebookGetRequest,
    NotebookUpdateRequest,
    NotebookDeleteRequest,
    NotebookListRequest,
    CreateCellRequest,
    CellIDRequest,
    DeleteCellResponse,
    Cell,
    UpdateCellRequest,
    ExecuteCellRequest,
    ExecuteCellResponse,
    NotebookListResponse,
    NotebookDeleteResponse,
    Output,
)
from datetime import datetime
import grpc
from concurrent import futures
from datetime import timezone
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from jupyter_notebook_protobuf.models import Base, NotebookModel, CellModel
from functools import wraps
import subprocess
import os
import redis
import logging

logger = logging.Logger(__name__)

# from .config.db_env import DATABASE_URL

NotebookDict = dict[int, Notebook]


redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)


def check_redis_connection():
    try:
        return redis_client.ping()
    except redis.exceptions.ConnectionError as e:
        logger.log(level=logging.WARN, msg=e)
        return False


# print(check_redis_connection())


def cache_notebook(f):
    """
    A decorator to cache the result of the given function for a given notebook ID.
    """

    @wraps(f)
    def wrapper(self, *args, **kwargs):
        # print(type(args[0]))
        request: NotebookGetRequest = args[0]
        redis_available = check_redis_connection()

        if request and redis_available:
            notebook: bytes = redis_client.get(f"notebook:{request.id}")

            if notebook is not None:
                return Notebook().FromString(notebook)

            notebook: Notebook = f(self, *args, **kwargs)

            if notebook:
                redis_client.set(f"notebook:{request.id}", notebook.SerializeToString())
                return notebook

        return f(self, *args, **kwargs)

    return wrapper


def provide_session(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        if hasattr(self, "session"):
            session: Session = self.session
        else:
            session: Session = sessionmaker(self.engine, autoflush=True)()
            self.session: Session = session

        try:
            result = f(self, session, *args, **kwargs)
            session.commit()
            return result
        except:
            session.rollback()
            raise
        finally:
            session.close()

    return wrapper


class NotebookService(NotebookServiceServicer):
    def __init__(self) -> None:
        self.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(self.engine)

    @provide_session
    def CreateNotebook(
        self,
        session: Session,
        request: NotebookCreateRequest,
        context: grpc.ServicerContext,
    ) -> Notebook:
        notebookModel = NotebookModel()

        session.add(notebookModel)
        session.flush()

        notebook = Notebook(
            id=notebookModel.id,
            name=request.name,
            author=request.author,
        )

        with open(f"notebooks/notebook_{notebookModel.id}.pb", "wb") as f:
            f.write(notebook.SerializeToString())

        return notebook

    @cache_notebook
    @provide_session
    def GetNotebook(
        self,
        session: Session,
        request: NotebookGetRequest,
        context: grpc.ServicerContext,
    ) -> Notebook:
        notebookModel: NotebookModel = session.get(NotebookModel, request.id)

        if notebookModel is None:
            context.abort(
                grpc.StatusCode.NOT_FOUND,
                "Notebook Not found. Invalid id.",
            )

        notebook = Notebook()
        with open(f"notebooks/notebook_{notebookModel.id}.pb", "rb") as f:
            notebook.ParseFromString(f.read())

        return notebook

    @provide_session
    def UpdateNotebook(
        self,
        session: Session,
        request: NotebookUpdateRequest,
        context: grpc.ServicerContext,
    ) -> Notebook:
        notebookModel: NotebookModel = session.query(NotebookModel).get(request.id)

        if notebookModel is None:
            context.abort(grpc.StatusCode.NOT_FOUND, "Notebook Not found. Invalid id.")

        notebookModel.updated = datetime.now(timezone.utc)

        notebook = Notebook()
        with open(f"notebooks/notebook_{notebookModel.id}.pb", "rb") as f:
            notebook.ParseFromString(f.read())

        return notebook

    @provide_session
    def DeleteNotebook(
        self,
        session: Session,
        request: NotebookDeleteRequest,
        context: grpc.ServicerContext,
    ) -> NotebookDeleteResponse:
        notebookModel: NotebookModel = session.query(NotebookModel).get(request.id)

        if notebookModel is None:
            context.abort(grpc.StatusCode.NOT_FOUND, "Notebook Not found. Invalid id.")

        session.delete(notebookModel)

        try:
            os.remove(f"notebooks/notebook_{notebookModel.id}.pb")
            return True
        except FileNotFoundError:
            return False

    @provide_session
    def ListNotebooks(
        self,
        session: Session,
        request: NotebookListRequest,
        context: grpc.ServicerContext,
    ) -> NotebookListResponse:
        notebookModels: list[NotebookModel] = session.query(NotebookModel).all()
        # return [
        #     Notebook().ParseFromString(
        #         open(f"notebooks/notebook_{notebookModel.id}.pb", "rb").read()
        #     )
        #     for notebookModel in notebookModels
        # ]
        response = []
        for notebookModel in notebookModels:
            notebook = Notebook()
            with open(f"notebooks/notebook_{notebookModel.id}.pb", "rb") as f:
                notebook.ParseFromString(f.read())
                response.append(notebook)
        return NotebookListResponse(notebooks=response)

    @provide_session
    def CreateCell(
        self,
        session: Session,
        request: CreateCellRequest,
        context: grpc.ServicerContext,
    ) -> Cell:
        cellModel = CellModel(notebook_id=request.notebook_id)
        session.add(cellModel)
        session.flush()

        cell = Cell(
            id=cellModel.id,
            type=request.type,
            source=request.source,
        )
        notebook = Notebook()

        with open(f"notebooks/notebook_{request.notebook_id}.pb", "rb") as f:
            notebook.ParseFromString(f.read())

        cell_entry = notebook.cells.get_or_create(cell.id)
        cell_entry.CopyFrom(cell)

        with open(f"notebooks/notebook_{request.notebook_id}.pb", "wb") as f:
            f.write(notebook.SerializeToString())

        return cell

    @provide_session
    def GetCell(
        self,
        session: Session,
        request: CellIDRequest,
        context: grpc.ServicerContext,
    ) -> Cell:
        cellModel: CellModel = session.query(CellModel).get(request.cell_id)

        if cellModel is None:
            context.abort(
                grpc.StatusCode.NOT_FOUND,
                "Cell Not found. Invalid id.",
            )
        notebook = Notebook()
        with open(f"notebooks/notebook_{cellModel.notebook_id}", "rb") as f:
            notebook.ParseFromString(f.read())

        return notebook.cells.get(key=cellModel.id)

    @provide_session
    def DeleteCell(
        self,
        session: Session,
        request: CellIDRequest,
        context: grpc.ServicerContext,
    ) -> DeleteCellResponse:
        cellModel: CellModel = session.query(cellModel).get(request.cell_id)

        if cellModel is None:
            context.abort(
                grpc.StatusCode.NOT_FOUND,
                "Cell Not found. Invalid id.",
            )

        session.delete(cellModel)

        notebook = Notebook()
        with open(f"notebooks/notebook_{cellModel.notebook_id}", "rb") as f:
            notebook.ParseFromString(f.read())

        return bool(cell := notebook.cells.pop(cellModel.id, None))

    @provide_session
    def UpdateCell(
        self,
        session: Session,
        request: UpdateCellRequest,
        context: grpc.ServicerContext,
    ) -> Cell:
        cellModel: CellModel = session.query(CellModel).get(request.cell_id)

        if cellModel is None:
            context.abort(
                grpc.StatusCode.NOT_FOUND,
                "Cell Not found. Invalid id.",
            )

        notebook = Notebook()
        with open(f"notebooks/notebook_{cellModel.notebook_id}", "rb") as f:
            notebook.ParseFromString(f.read())

        return notebook.cells.get(key=cellModel.id)

    @provide_session
    def ExecuteCell(
        self,
        session: Session,
        request: ExecuteCellRequest,
        context: grpc.ServicerContext,
    ) -> ExecuteCellResponse:
        cellModel: CellModel = session.get(CellModel, request.cell_id)

        if cellModel is None:
            context.abort(
                grpc.StatusCode.NOT_FOUND,
                "Cell Not found. Invalid id.",
            )

        notebook = Notebook()
        with open(f"notebooks/notebook_{cellModel.notebook_id}.pb", "rb") as f:
            notebook.ParseFromString(f.read())

        cell = notebook.cells.get(key=cellModel.id)

        code_type: Cell.Type = cell.type
        if code_type == Cell.CODE:
            ### Execute the cell in an environment.
            with open("/tmp/cell.py", "w") as f:
                f.write(cell.source)

            process = subprocess.Popen(
                ["python", "/tmp/cell.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            stdout, stderr = process.communicate()

            errors = Output(type=Output.ERROR, text=stderr.decode("utf-8"))
            result = Output(type=Output.EXECUTE_RESULT, text=stdout.decode("utf-8"))

        return ExecuteCellResponse(output=[errors, result])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_NotebookServiceServicer_to_server(NotebookService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
