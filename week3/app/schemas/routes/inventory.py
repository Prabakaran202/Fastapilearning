from fastapi import APIRouter,HTTPException,Path,Query
from schemas.inventory import addPro


DB = [
    {"id": 1, "name": "Laptop", "price": 5000, "stock": 5, "category": "Electronics"},
    {"id": 2, "name": "Mouse", "price": 500, "stock": 0, "category": "Electronics"},
    {"id": 3, "name": "Monitor", "price": 8000, "stock": 2, "category": "Electronics"},
    {"id": 4, "name": "Keyboard", "price": 1200, "stock": 0, "category": "Electronics"}
]


router = APIRouter(prefix="/inventory",tags=["inventory"])


@router.get("/")
async def getall():
    return DB
  
@router.get("/search/")
async def minmax_item(min_price: int = Query(..., gt=0), 
    max_price: int = Query(..., le=10000)):
    
    relt=[]

    for item in DB:

        if item["price"] >=min_price and item["price"] <=max_price:
            relt.append(item)
    if not relt:
        return{"mag":"your items not found"}
    
    return {"msg":"your items is","data":relt}

@router.get("/out-of-stock/{outofstock}")
async def stockof(item:int = 0):
    relt=[]

    for items in DB:
        if items["stock"] == item : 
            relt.append(items["name"])
    if not relt:
        return{"mag":"your items not found"}
    
    return {"msg":"your items is","data":relt}

@router.post("/add")
async def addnew(new:addPro):
    return {"msg":"new user add succeful","data":new}
   
