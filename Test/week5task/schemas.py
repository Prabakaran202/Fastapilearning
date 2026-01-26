
from pydantic import BaseModel, Field




class UserSchema(BaseModel):
     name: str = Field(..., title="name", max_length=40)
     Class: str = Field(..., title="class", max_length=10)