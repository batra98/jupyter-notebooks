from .base import Base, intpk, str64
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils.models import Timestamp
from protoc.gen.notebook_pb2 import Notebook
from sqlalchemy import Integer, String


class NotebookModel(Base, Timestamp):
    __tablename__ = "notebooks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    cells = relationship("CellModel", back_populates="notebook")
