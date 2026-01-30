
from pydantic import BaseModel, Field


class UserSchema(BaseModel):
     name: str = Field(..., title="name", max_length=40)
     Class:str= Field(..., title="Class", max_length=10)
     mark: float = Field(..., title="mark", ge=0, le=100)


class user(BaseModel):
     name: str
     mark: float
     Class: str
    