Readme for Notebook gRPC API

This is a Notebook gRPC API implemented in Python. It allows users to create, read, update, and delete notebooks, as well as create, read, update, and delete cells within the notebooks. It uses the Notebook protobuf messages and gRPC services to communicate between client and server.



## Installation
This project uses poetry for dependency management.

1. Clone the repository
2. Install dependencies with `poetry install`
4. Set up the database URL in `config/db_env.py`
5. Run the server with `python server.py`

## Usage
Once the server is running, you can use the Notebook gRPC API to interact with notebooks and cells. You can use the Notebook gRPC client to interact with the server or use any gRPC client of your choice.

A sample client is given in `client.py`. Run the client with this command `python client.py`.

## Supported methods

### CreateNotebook
Create a new notebook.

### GetNotebook
Get an existing notebook by ID.

### UpdateNotebook
Update an existing notebook.

### DeleteNotebook
Delete an existing notebook.

### ListNotebooks
List all existing notebooks.

### CreateCell
Create a new cell in a notebook.

### GetCell
Get an existing cell by ID.

### UpdateCell
Update an existing cell.

### DeleteCell
Delete an existing cell.

### ExecuteCell
Execute the source code in a cell and return the output.


## License
This project is licensed under the MIT License.