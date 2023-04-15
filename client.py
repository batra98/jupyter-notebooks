from build.gen.notebook_pb2 import Notebook, Cell, Output
from build.gen.notebook_pb2_grpc import NotebookServiceStub
import grpc

channel = grpc.insecure_channel("localhost:50052")
stub = NotebookServiceStub(channel=channel)

# Create a new notebook
notebook: Notebook = Notebook()
notebook.name = "My Notebook"
notebook.author = "John Doe"

response = stub.CreateNotebook(notebook)
print(response)


# # Add a cell to the notebook
# cell: Cell = notebook.cells.add()
# cell.type = Cell.Type.CODE
# cell.source = "print('Hello, world!')"

# output: Output = cell.outputs.add()
# output.type = Output.Type.DISPLAY_DATA
# output.text = "Hello World!"
