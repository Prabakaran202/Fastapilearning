
from fastapi import APIRouter,Path,Query,HTTPException



from schemas import UserSchema,user

router = APIRouter()

@router.post("/create_user/{name}/mark/{mark}", response_model=user)
async def create_user(name: str = Path(..., title="The name of the user"), 
                      mark: float = Path(..., title="The mark of the user"),query: str = Query(None, title="The query string")):
    if mark < 0 or mark > 100:
        raise HTTPException(status_code=400, detail="Mark must be between 0 and 100")
    user_data = user(name=name, mark=mark, Class=query)
    return user_data