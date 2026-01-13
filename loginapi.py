from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app=FastAPI()
class User(BaseModel):
    name:str
    pas:str
class check(BaseModel):
    msg:str
    pas:Optional[User] = None

@app.post("/login/",response_model=check)
async def login(user:User):
    return {"msg":"creat succ","user":user}