from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils.models import Timestamp
from sqlalchemy import Integer


class NotebookModel(Base, Timestamp):
    __tablename__ = "notebooks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    cells = relationship("CellModel", back_populates="notebook")
