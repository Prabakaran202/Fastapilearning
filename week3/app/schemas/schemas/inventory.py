from pydantic import BaseModel,Field

class Product(BaseModel):
    id:int
    name:str=Field(...,min_length=3)
    price:float=Field(...,gt=0)
    stock:int=Field(...,ge=0)
    category:str
class addPro(BaseModel):
    id:int
    name:str