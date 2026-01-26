
from fastapi import APIRouter

from schemas import UserSchema

router = APIRouter()
@router.post("/users/", response_model=UserSchema)
async def create_user(user: UserSchema):
    return user