from fastapi import APIRouter

from starlette.responses import JSONResponse

from .user.views import router as user_router
from .book.views import router as book_router

api_router = APIRouter(
    default_response_class=JSONResponse,
)

api_router.include_router(
    user_router, prefix="/users", tags=["users"]
)

api_router.include_router(
    book_router, prefix="/books", tags=["books"]
)