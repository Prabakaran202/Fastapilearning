
from pydantic import BaseModel, Field




class UserSchema(BaseModel):
     name: str = Field(..., title="name", max_length=40)
     mark: float = Field(..., title="mark", ge=0, le=100)