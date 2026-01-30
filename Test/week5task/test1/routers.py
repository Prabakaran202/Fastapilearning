
from fastapi import APIRouter,Path, Query

from schemas import UserSchema

router = APIRouter()
@router.post("/users/{Mark}/{Name}")
async def create_user(Mark: UserSchema =Path(..., title="Mark", ge=0, le=100),q:str=Query(None, title="Query", max_length=50),Name:UserSchema=Path(..., title="Name", max_length=40)):
    return {"Mark": Mark, "Name": Name, "q": q}