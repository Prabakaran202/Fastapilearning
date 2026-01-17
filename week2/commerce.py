from fastapi import FastAPI,Path,Query
from pydantic import BaseModel,Field

app=FastAPI()

class Product(BaseModel):
    name: str = Field(..., min_length=3)
    price: float = Field(..., gt=0,le=10000) # gt = Greater Than
    tags: list[int] = []
ProductDB = [
    {"name": "Mouse", "price": 500, "tags": ["electronics", "pc"]},
    {"name": "Keyboard", "price": 1200, "tags": ["electronics", "pc"]},
    {"name": "USB Cable", "price": 300, "tags": ["mobile", "accessories"]},
    {"name": "Power Bank", "price": 1500, "tags": ["mobile", "gadget"]},
    {"name": "Headphones", "price": 2500, "tags": ["audio", "electronics"]},
    {"name": "Web Cam", "price": 3500, "tags": ["video", "pc"]},
    {"name": "Laptop Stand", "price": 1200, "tags": ["accessories", "office"]},
    {"name": "Mouse Pad", "price": 400, "tags": ["pc", "accessories"]},
    {"name": "Bluetooth Speaker", "price": 4500, "tags": ["audio", "gadget"]},
    {"name": "Gaming Chair", "price": 9500, "tags": ["furniture", "pc"]}
]
@app.post("/items/adddata/")
async def add_new(adddata:Product):
    ProductDB.append(adddata.model_dump())
    return {"msg":"your datas","adddata":adddata}
    