from typing import List, Optional
from sqlalchemy import Column, Integer, String

from ..models import LMSBaseModel
from ..database.core import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class UserBase(LMSBaseModel):
    id : int
    name : str

class UserRead(UserBase):
    pass

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserDelete(UserBase):
    pass

class UserList(LMSBaseModel):
    items : Optional[List[UserRead]] = []
