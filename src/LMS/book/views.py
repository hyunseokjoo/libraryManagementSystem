from fastapi import APIRouter

router = APIRouter()


@router.get("")
def get_test():
    return {"message": "book test 입니다."}
