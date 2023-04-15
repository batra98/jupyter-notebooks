from build.gen.notebook_pb2_grpc import (
    NotebookServiceServicer,
    add_NotebookServiceServicer_to_server,
)
from build.gen.notebook_pb2 import Notebook
from datetime import datetime
import grpc
from concurrent import futures


class NotebookService(NotebookServiceServicer):
    def CreateNotebook(self, request, context):
        author: str = request.author
        name: str = request.name
        created_time: datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cells: list = []

        return Notebook(
            name=name,
            author=author,
            created=created_time,
            modified=created_time,
            cells=cells,
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_NotebookServiceServicer_to_server(NotebookService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
