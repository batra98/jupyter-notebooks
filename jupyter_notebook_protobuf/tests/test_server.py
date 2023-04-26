import unittest
import grpc
import time

# Import the generated gRPC classes
from protoc.gen import notebook_pb2, notebook_pb2_grpc


# Import the server implementation
from server import NotebookServicer

class NotebookServerTestCase(unittest.TestCase):
    
    def setUp(self):
        # Set up the server with the NotebookServicer implementation
        self.server = grpc.server(thread_pool=None)
        notebook_pb2_grpc.add_NotebookServicer_to_server(NotebookServicer(), self.server)
        self.server.add_insecure_port('[::]:50051')
        self.server.start()

        # Create a gRPC channel to communicate with the server
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = notebook_pb2_grpc.NotebookStub(self.channel)
        
    def tearDown(self):
        # Stop the server after each test case
        self.server.stop(0)
        
    def test_create_notebook(self):
        # Test creating a new notebook
        request = notebook_pb2.CreateNotebookRequest(name="Test Notebook")
        response = self.stub.CreateNotebook(request)
        self.assertIsNotNone(response.id)
        
    def test_get_notebook(self):
        # Test getting an existing notebook
        create_request = notebook_pb2.CreateNotebookRequest(name="Test Notebook")
        create_response = self.stub.CreateNotebook(create_request)
        notebook_id = create_response.id
        
        get_request = notebook_pb2.GetNotebookRequest(id=notebook_id)
        get_response = self.stub.GetNotebook(get_request)
        self.assertEqual(get_response.notebook.id, notebook_id)
        self.assertEqual(get_response.notebook.name, "Test Notebook")
        
    def test_update_notebook(self):
        # Test updating an existing notebook
        create_request = notebook_pb2.CreateNotebookRequest(name="Test Notebook")
        create_response = self.stub.CreateNotebook(create_request)
        notebook_id = create_response.id
        
        update_request = notebook_pb2.UpdateNotebookRequest(id=notebook_id, name="Updated Test Notebook")
        update_response = self.stub.UpdateNotebook(update_request)
        self.assertEqual(update_response.notebook.id, notebook_id)
        self.assertEqual(update_response.notebook.name, "Updated Test Notebook")
        
    def test_delete_notebook(self):
        # Test deleting an existing notebook
        create_request = notebook_pb2.CreateNotebookRequest(name="Test Notebook")
        create_response = self.stub.CreateNotebook(create_request)
        notebook_id = create_response.id
        
        delete_request = notebook_pb2.DeleteNotebookRequest(id=notebook_id)
        delete_response = self.stub.DeleteNotebook(delete_request)
        self.assertEqual(delete_response.id, notebook_id)
        
    def test_list_notebooks(self):
        # Test listing all existing notebooks
        create_request_1 = notebook_pb2.CreateNotebookRequest(name="Test Notebook 1")
        create_request_2 = notebook_pb2.CreateNotebookRequest(name="Test Notebook 2")
        create_response_1 = self.stub.CreateNotebook(create_request_1)
        create_response_2 = self.stub.CreateNotebook(create_request_2)
        
        list_request = notebook_pb2.ListNotebooksRequest()
        list_response = self.stub.ListNotebooks(list_request)
        self.assertEqual(len(list_response.notebooks), 2)
        self.assertEqual(list_response.notebooks[0].name, "Test Notebook 1")
        self.assertEqual(list_response.notebooks[1].name, "Test Notebook 2")
        
    def test_create_cell(self):
        # Test creating a new cell in a notebook
        create_request = notebook_pb2.CreateNotebookRequest(name="
