from protoc.gen.notebook_pb2 import (
    Notebook,
    Cell,
    Output,
    NotebookCreateRequest,
    NotebookGetRequest,
    CreateCellRequest,
    ExecuteCellRequest,
    ExecuteCellResponse,
    NotebookListRequest,
    NotebookListResponse,
)
from protoc.gen.notebook_pb2_grpc import NotebookServiceStub
import grpc

channel = grpc.insecure_channel("localhost:50052")
stub = NotebookServiceStub(channel=channel)

# Create a new notebook
notebookCreateRequest: NotebookCreateRequest = NotebookCreateRequest()
notebookCreateRequest.name = "My Notebook"
notebookCreateRequest.author = "John Doe"

notebook: Notebook = stub.CreateNotebook(notebookCreateRequest)
print(
    f"New Notebook Created with the following details: \n Id: {notebook.id} \n Name: {notebook.name} \n Author: {notebook.author}"
)


notebookGetRequest: NotebookGetRequest = NotebookGetRequest(id=notebook.id)
notebookGet: Notebook = stub.GetNotebook(notebookGetRequest)

print(notebookGet)
print(notebookGet == notebook)


# Add a cell to the notebook
cellCreateRequest: CreateCellRequest = CreateCellRequest(
    notebook_id=notebook.id,
    type=Cell.CODE,
    source="printf('Hello, world!')",
)


cell: Cell = stub.CreateCell(cellCreateRequest)
print(
    f"New Cell Created with the following details: \n Id: {cell.id} \n Type: {cell.type} \n Source: {cell.source}"
)

print(notebook.cells)


notebookListRequest: NotebookListRequest = NotebookListRequest()

notebooks: NotebookListResponse = stub.ListNotebooks(notebookListRequest)
print(notebooks)


cellExecuteRequest: ExecuteCellRequest = ExecuteCellRequest(
    notebook_id=notebook.id,
    cell_id=cell.id,
)

cell_response: ExecuteCellResponse = stub.ExecuteCell(cellExecuteRequest)

print(f"Executed the cell. \n {cell_response}")

notebookGetRequest: NotebookGetRequest = NotebookGetRequest(id=notebook.id)
notebookGet: Notebook = stub.GetNotebook(notebookGetRequest)
print(notebookGet.cells)

# output: Output = cell.outputs.add()
# output.type = Output.Type.DISPLAY_DATA
# output.text = "Hello World!"
