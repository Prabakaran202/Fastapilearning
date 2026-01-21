
from schemas.inventory import Product,addPro
from fastapi import APIRouter,HTTPException

DB = [
    {"id": 1, "name": "Laptop", "price": 50000, "stock": 5, "category": "Electronics"},
    {"id": 2, "name": "Mouse", "price": 500, "stock": 0, "category": "Electronics"},
    {"id": 3, "name": "Monitor", "price": 8000, "stock": 2, "category": "Electronics"},
    {"id": 4, "name": "Keyboard", "price": 1200, "stock": 0, "category": "Electronics"}
]


router = APIRouter(prefix="/inventory",tags=["inventory"])


@router.get("/")
async def getall():
    return DB
  
