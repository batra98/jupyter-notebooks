from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import Integer, String, ForeignKey

intpk = mapped_column(Integer, primary_key=True)
str64 = mapped_column(String(64))
notebookfk = mapped_column(Integer, ForeignKey("notebooks.id"), nullable=False)


class Base(DeclarativeBase):
    pass
