from .base import Base, intpk, str64, notebookfk
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils.models import Timestamp
from protoc.gen.notebook_pb2 import Cell
from sqlalchemy import Integer, ForeignKey, String


class CellModel(Base, Timestamp):
    __tablename__ = "cells"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    notebook_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("notebooks.id"), nullable=False
    )
    # cell_type: Mapped[int] = mapped_column(Integer, nullable=True)
    # source: Mapped[str] = mapped_column(String(64), nullable=True)
    notebook = relationship("NotebookModel", back_populates="cells")
