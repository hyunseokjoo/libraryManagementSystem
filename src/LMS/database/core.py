import re
from typing import Annotated

from fastapi import Depends
from pydantic import BaseModel
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import Session, sessionmaker
from starlette.requests import Request

from LMS.config import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db(request: Request):
    return request.state.db


DbSession = Annotated[Session, Depends(get_db)]
