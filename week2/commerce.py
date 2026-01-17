from fastapi import FastAPI,Path,Query
from pydantic import BaseModel,Field

app=FastAPI()

class Product(BaseModel):
    name: str = Field(..., min_length=3)
    price: int= Field(..., gt=0,le=10000) # gt = Greater Than
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
'''
@app.get("/items/choiceprice/")
async def choiceprice(cprice:int=Path(...,title="filer price",ge=1,le=200000),q:str|None=Query(...,min_length=4,max_length=50)):
    for cp in ProductDB:
     if  cprice == cp["price"]:
        return {"msg":cp}
    return {"msg":"your product"}'''

@app.get("/items/choiceprice/")
async def choiceprice(
    min_price: int = Query(..., gt=0), 
    max_price: int = Query(..., le=10000)
):
    results = [] # மேட்ச் ஆகுற பொருட்களைச் சேமிக்க ஒரு காலி லிஸ்ட்
    
    for item in ProductDB:
        # விலை min_price-க்கும் max_price-க்கும் நடுவுல இருக்கானு செக் பண்றோம்
        if item["price"] >= min_price and item["price"] <= max_price:
            results.append(item) # மேட்ச் ஆனா லிஸ்ட்ல சேர்த்துக்கோங்க
            
    if not results:
        return {"msg": "இந்த பட்ஜெட்ல பொருட்கள் ஏதும் இல்லை"}
        
    return {"msg": "உங்க பட்ஜெட்டுக்கு ஏத்த பொருட்கள் இதோ", "data": results}