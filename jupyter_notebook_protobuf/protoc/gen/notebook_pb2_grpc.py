# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import notebook_pb2 as notebook__pb2


class NotebookServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateNotebook = channel.unary_unary(
            "/NotebookService/CreateNotebook",
            request_serializer=notebook__pb2.NotebookCreateRequest.SerializeToString,
            response_deserializer=notebook__pb2.Notebook.FromString,
        )
        self.GetNotebook = channel.unary_unary(
            "/NotebookService/GetNotebook",
            request_serializer=notebook__pb2.NotebookGetRequest.SerializeToString,
            response_deserializer=notebook__pb2.Notebook.FromString,
        )
        self.UpdateNotebook = channel.unary_unary(
            "/NotebookService/UpdateNotebook",
            request_serializer=notebook__pb2.NotebookUpdateRequest.SerializeToString,
            response_deserializer=notebook__pb2.Notebook.FromString,
        )
        self.DeleteNotebook = channel.unary_unary(
            "/NotebookService/DeleteNotebook",
            request_serializer=notebook__pb2.NotebookDeleteRequest.SerializeToString,
            response_deserializer=notebook__pb2.NotebookDeleteResponse.FromString,
        )
        self.ListNotebooks = channel.unary_unary(
            "/NotebookService/ListNotebooks",
            request_serializer=notebook__pb2.NotebookListRequest.SerializeToString,
            response_deserializer=notebook__pb2.NotebookListResponse.FromString,
        )
        self.CreateCell = channel.unary_unary(
            "/NotebookService/CreateCell",
            request_serializer=notebook__pb2.CreateCellRequest.SerializeToString,
            response_deserializer=notebook__pb2.Cell.FromString,
        )
        self.GetCell = channel.unary_unary(
            "/NotebookService/GetCell",
            request_serializer=notebook__pb2.CellIDRequest.SerializeToString,
            response_deserializer=notebook__pb2.Cell.FromString,
        )
        self.UpdateCell = channel.unary_unary(
            "/NotebookService/UpdateCell",
            request_serializer=notebook__pb2.UpdateCellRequest.SerializeToString,
            response_deserializer=notebook__pb2.Cell.FromString,
        )
        self.DeleteCell = channel.unary_unary(
            "/NotebookService/DeleteCell",
            request_serializer=notebook__pb2.CellIDRequest.SerializeToString,
            response_deserializer=notebook__pb2.DeleteCellResponse.FromString,
        )
        self.ExecuteCell = channel.unary_unary(
            "/NotebookService/ExecuteCell",
            request_serializer=notebook__pb2.ExecuteCellRequest.SerializeToString,
            response_deserializer=notebook__pb2.ExecuteCellResponse.FromString,
        )


class NotebookServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateNotebook(self, request, context):
        """Creates a new notebook with the specified name and author"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetNotebook(self, request, context):
        """Retrieves the notebook with the specified id"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateNotebook(self, request, context):
        """Updates the notebook with the specified name and author"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteNotebook(self, request, context):
        """Deletes the notebook with the specified id"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListNotebooks(self, request, context):
        """Retrieves the list of all notebooks"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateCell(self, request, context):
        """Creates a new cell in an existing notebook"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetCell(self, request, context):
        """Retrieves an existing cell by its ID"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateCell(self, request, context):
        """Updates an existing cell by its ID"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteCell(self, request, context):
        """Deletes an existing cell by its ID"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExecuteCell(self, request, context):
        """Executes a cell and returns its output"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_NotebookServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateNotebook": grpc.unary_unary_rpc_method_handler(
            servicer.CreateNotebook,
            request_deserializer=notebook__pb2.NotebookCreateRequest.FromString,
            response_serializer=notebook__pb2.Notebook.SerializeToString,
        ),
        "GetNotebook": grpc.unary_unary_rpc_method_handler(
            servicer.GetNotebook,
            request_deserializer=notebook__pb2.NotebookGetRequest.FromString,
            response_serializer=notebook__pb2.Notebook.SerializeToString,
        ),
        "UpdateNotebook": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateNotebook,
            request_deserializer=notebook__pb2.NotebookUpdateRequest.FromString,
            response_serializer=notebook__pb2.Notebook.SerializeToString,
        ),
        "DeleteNotebook": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteNotebook,
            request_deserializer=notebook__pb2.NotebookDeleteRequest.FromString,
            response_serializer=notebook__pb2.NotebookDeleteResponse.SerializeToString,
        ),
        "ListNotebooks": grpc.unary_unary_rpc_method_handler(
            servicer.ListNotebooks,
            request_deserializer=notebook__pb2.NotebookListRequest.FromString,
            response_serializer=notebook__pb2.NotebookListResponse.SerializeToString,
        ),
        "CreateCell": grpc.unary_unary_rpc_method_handler(
            servicer.CreateCell,
            request_deserializer=notebook__pb2.CreateCellRequest.FromString,
            response_serializer=notebook__pb2.Cell.SerializeToString,
        ),
        "GetCell": grpc.unary_unary_rpc_method_handler(
            servicer.GetCell,
            request_deserializer=notebook__pb2.CellIDRequest.FromString,
            response_serializer=notebook__pb2.Cell.SerializeToString,
        ),
        "UpdateCell": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateCell,
            request_deserializer=notebook__pb2.UpdateCellRequest.FromString,
            response_serializer=notebook__pb2.Cell.SerializeToString,
        ),
        "DeleteCell": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteCell,
            request_deserializer=notebook__pb2.CellIDRequest.FromString,
            response_serializer=notebook__pb2.DeleteCellResponse.SerializeToString,
        ),
        "ExecuteCell": grpc.unary_unary_rpc_method_handler(
            servicer.ExecuteCell,
            request_deserializer=notebook__pb2.ExecuteCellRequest.FromString,
            response_serializer=notebook__pb2.ExecuteCellResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "NotebookService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class NotebookService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateNotebook(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/NotebookService/CreateNotebook",
            notebook__pb2.NotebookCreateRequest.SerializeToString,
            notebook__pb2.Notebook.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetNotebook(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/NotebookService/GetNotebook",
            notebook__pb2.NotebookGetRequest.SerializeToString,
            notebook__pb2.Notebook.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateNotebook(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/NotebookService/UpdateNotebook",
            notebook__pb2.NotebookUpdateRequest.SerializeToString,
            notebook__pb2.Notebook.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteNotebook(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/NotebookService/DeleteNotebook",
            notebook__pb2.NotebookDeleteRequest.SerializeToString,
            notebook__pb2.NotebookDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListNotebooks(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/NotebookService/ListNotebooks",
            notebook__pb2.NotebookListRequest.SerializeToString,
            notebook__pb2.NotebookListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateCell(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/NotebookService/CreateCell",
            notebook__pb2.CreateCellRequest.SerializeToString,
            notebook__pb2.Cell.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetCell(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/NotebookService/GetCell",
            notebook__pb2.CellIDRequest.SerializeToString,
            notebook__pb2.Cell.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateCell(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/NotebookService/UpdateCell",
            notebook__pb2.UpdateCellRequest.SerializeToString,
            notebook__pb2.Cell.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteCell(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/NotebookService/DeleteCell",
            notebook__pb2.CellIDRequest.SerializeToString,
            notebook__pb2.DeleteCellResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ExecuteCell(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/NotebookService/ExecuteCell",
            notebook__pb2.ExecuteCellRequest.SerializeToString,
            notebook__pb2.ExecuteCellResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
