from typing import Optional, List

from sqlalchemy import Column, Integer, String, Boolean

from LMS.models import LMSBaseModel
from LMS.database.core import Base


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    borrowed = Column(Boolean)


class BookBase(LMSBaseModel):
    id : int
    title : str
    author : str
    borrowed : bool
    borrowing_userid : int

class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookDelete(BookBase):
    pass

class BookList(BookBase):
    items : Optional[List[BookRead]] = []

