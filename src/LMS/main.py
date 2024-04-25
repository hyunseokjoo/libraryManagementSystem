from uuid import uuid1
from typing import Optional, Final
from contextvars import ContextVar
from fastapi import FastAPI

from sqlalchemy.orm import scoped_session
from starlette.requests import Request

from .api import api_router
from .config import SQLALCHEMY_DATABASE_URL
from .database.core import engine, sessionmaker

app = FastAPI()

app.include_router(api_router)

@app.get('/')
async def root():
    return {"message" : "도서 관리 백엔드 입니다."}

REQUEST_ID_CTX_KEY: Final[str] = "request_id"
_request_id_ctx_var: ContextVar[Optional[str]] = ContextVar(REQUEST_ID_CTX_KEY, default=None)

def get_request_id() -> Optional[str]:
    return _request_id_ctx_var.get()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request_id = str(uuid1())

    # we create a per-request id such that we can ensure that our session is scoped for a particular request.
    # see: https://github.com/tiangolo/fastapi/issues/726
    ctx_token = _request_id_ctx_var.set(request_id)

    try:
        session = scoped_session(sessionmaker(bind=engine), scopefunc=get_request_id)
        request.state.db = session()
        response = await call_next(request)
    except Exception as e:
        raise e from None
    finally:
        request.state.db.close()

    _request_id_ctx_var.reset(ctx_token)
    return response