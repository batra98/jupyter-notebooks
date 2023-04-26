from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Cell(_message.Message):
    __slots__ = ["id", "outputs", "source", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CODE: Cell.Type
    ID_FIELD_NUMBER: _ClassVar[int]
    MARKDOWN: Cell.Type
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    outputs: _containers.RepeatedCompositeFieldContainer[Output]
    source: str
    type: Cell.Type
    def __init__(self, id: _Optional[int] = ..., type: _Optional[_Union[Cell.Type, str]] = ..., source: _Optional[str] = ..., outputs: _Optional[_Iterable[_Union[Output, _Mapping]]] = ...) -> None: ...

class CellIDRequest(_message.Message):
    __slots__ = ["cell_id", "notebook_id"]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    cell_id: int
    notebook_id: int
    def __init__(self, notebook_id: _Optional[int] = ..., cell_id: _Optional[int] = ...) -> None: ...

class CreateCellRequest(_message.Message):
    __slots__ = ["notebook_id", "source", "type"]
    NOTEBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    notebook_id: int
    source: str
    type: Cell.Type
    def __init__(self, notebook_id: _Optional[int] = ..., type: _Optional[_Union[Cell.Type, str]] = ..., source: _Optional[str] = ...) -> None: ...

class DeleteCellResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ExecuteCellRequest(_message.Message):
    __slots__ = ["cell_id", "notebook_id"]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    cell_id: int
    notebook_id: int
    def __init__(self, notebook_id: _Optional[int] = ..., cell_id: _Optional[int] = ...) -> None: ...

class ExecuteCellResponse(_message.Message):
    __slots__ = ["output"]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    output: _containers.RepeatedCompositeFieldContainer[Output]
    def __init__(self, output: _Optional[_Iterable[_Union[Output, _Mapping]]] = ...) -> None: ...

class Notebook(_message.Message):
    __slots__ = ["author", "cells", "created", "id", "name", "updated"]
    class CellsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Cell
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Cell, _Mapping]] = ...) -> None: ...
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    author: str
    cells: _containers.MessageMap[int, Cell]
    created: str
    id: int
    name: str
    updated: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., author: _Optional[str] = ..., created: _Optional[str] = ..., updated: _Optional[str] = ..., cells: _Optional[_Mapping[int, Cell]] = ...) -> None: ...

class NotebookCreateRequest(_message.Message):
    __slots__ = ["author", "name"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    author: str
    name: str
    def __init__(self, name: _Optional[str] = ..., author: _Optional[str] = ...) -> None: ...

class NotebookDeleteRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class NotebookDeleteResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class NotebookGetRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class NotebookListRequest(_message.Message):
    __slots__ = ["limit", "offset"]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class NotebookListResponse(_message.Message):
    __slots__ = ["notebooks"]
    NOTEBOOKS_FIELD_NUMBER: _ClassVar[int]
    notebooks: _containers.RepeatedCompositeFieldContainer[Notebook]
    def __init__(self, notebooks: _Optional[_Iterable[_Union[Notebook, _Mapping]]] = ...) -> None: ...

class NotebookUpdateRequest(_message.Message):
    __slots__ = ["author", "id", "name"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    author: str
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., author: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class Output(_message.Message):
    __slots__ = ["text", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DISPLAY_DATA: Output.Type
    ERROR: Output.Type
    EXECUTE_RESULT: Output.Type
    STREAM: Output.Type
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    text: str
    type: Output.Type
    def __init__(self, type: _Optional[_Union[Output.Type, str]] = ..., text: _Optional[str] = ...) -> None: ...

class UpdateCellRequest(_message.Message):
    __slots__ = ["cell_id", "notebook_id", "source", "type"]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    cell_id: int
    notebook_id: int
    source: str
    type: Cell.Type
    def __init__(self, notebook_id: _Optional[int] = ..., cell_id: _Optional[int] = ..., type: _Optional[_Union[Cell.Type, str]] = ..., source: _Optional[str] = ...) -> None: ...
