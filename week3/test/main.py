

from fastapi import FastAPI,Path,Query
from pydantic import BaseModel


app=FastAPI()


class bookstor(BaseModel):
    name:str
    aurthor:str
    price:int


db=[{"name":"nadaipayanam","aurthor":"praba","price":200},{"name":"unakenna","aurthor":"vetri","price":300},{"name":"nadipin kadhal","aurthor":"vadivu","price":200}]


@app.post("/list/")

def new(add:bookstor):
    db.append(add.model_dump())  
    return{"msg":"hello wait naa msg panarathu"}


@app.get("/list/{id}")
def find(id:str):
    new=[]
    for i in db:
        if i["aurthor"] == id:
            new.append(i["name"])
            return{"msg":"youfind aurther book ","book":new}
    return {"msg":"our auorthoe book not find "}    

