from fastapi import APIRouter

from shemas import userRequest, userResponse 

router = APIRouter()
@router.post("/create_user", response_model=userResponse)
async def create_user(user: userRequest):
    # Simulate user creation logic
    new_user = userResponse(
        id=1,
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        is_active=True,
        is_superuser=False,
        is_verified=False,
        created_at="2024-01-01T00:00:00Z",
        updated_at="2024-01-01T00:00:00Z",
        deleted_at=None
    )
    return new_user
@router.get("/get_user/{user_id}", response_model=userResponse)
async def get_user(user_id: int):
    # Simulate fetching user logic
    fetched_user = userResponse(
        id=user_id,
        username="johndoe",
        email="johndoe@example.com",
        full_name="John Doe",
        is_active=True,
        is_superuser=False,
        is_verified=True,
        created_at="2023-01-01T00:00:00Z",
        updated_at="2023-06-01T00:00:00Z",
        deleted_at=None
    )
    return fetched_user