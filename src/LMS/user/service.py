from typing import Optional, List
from LMS.database.core import DbSession
from .models import User, UserCreate, UserUpdate

def get(*, db_session, user_id: int) -> Optional[User]:
    return db_session.query(User).filter(User.id == user_id).first()

def get_all(*, db_session, limit=100):
    return {
        "items" : db_session.query(User).all()
    }

def create(*, db_session, user_in: UserCreate) -> User:
    user = User(**user_in.dict())
    db_session.add(user)
    db_session.commit()
    return user

def update(*, db_session, user: User, user_in: UserUpdate) -> User:
    user_data = user.__dict__
    update_data = user_in.dict()
    for field in user_data:
        if field in update_data:
            setattr(user, field, update_data[field])

    db_session.commit()
    return user

def delete(*, db_session, user_id: int):
    user = db_session.query(User).filter(User.id == user_id)
    db_session.delete(user)
    db_session.commit()