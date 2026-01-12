from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()

class User(BaseModel):
    username: str
    email: str
    age: int
@app.get('/')
async def mynear(username:str,email:str,age:int):
    
    return {
       "Name" : username,
        "email":email,
        'age':age
    }
@app.get("/items/{iterm_id}")
async def iterms(iterm_id:int):
    
    return {"iterm":iterm_id,'message':"this message for this iterm name"}
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}