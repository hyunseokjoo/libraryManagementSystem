from typing import List
from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import IntegrityError

from .service import get, get_all, create, update, delete
from .models import UserRead, UserUpdate, UserCreate, UserDelete, UserList
from LMS.database.core import DbSession


router = APIRouter()

@router.get("/", response_model=UserList)
def get_users(db_session: DbSession):
    user = get_all(db_session=db_session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "유저가 없습니다."}]
        )
    return user

@router.get("/{user_id}", response_model=UserRead)
def get_user(db_session: DbSession, user_id):
    user = get(db_session=db_session, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "유저가 없습니다."}]
        )
    return user

@router.post("", response_model=UserRead)
def create_user(db_session: DbSession, user_in: UserCreate):
    user = get(db_session=db_session, user_id=user_in.id)
    if user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "유저가 이미 존재 합니다."}],
        )
    user = create(db_session=db_session, user_in=user_in)
    return user

@router.put("/{user_id}", response_model=UserRead)
def update_user(db_session: DbSession, user_id, user_in: UserUpdate):
    user = get(db_session=db_session, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "유저가 없습니다."}],
        )
    user = update(db_session=db_session, user=user, user_in=user_in)
    return user

@router.delete("/{user_id}", response_model=None)
def delete_user(db_session: DbSession, user_in: UserDelete):
    user = get(db_session=db_session, user_id=user_in.id)
    if user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "유저가 없습니다."}],
        )
    delete(db_session=db_session, user_id=user_in.id)