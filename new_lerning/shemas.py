from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float 

class User(BaseModel):

    username: str
    email: str
    full_name: str 

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

class Order(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    total_price: float
    user_id: int
class userRequest(BaseModel):
    username:str
    email:str
    full_name:str
class userResponse(BaseModel):
    id:int
    username:str
    email:str
    full_name:str
    is_active:bool
    is_superuser:bool
    is_verified:bool
    created_at:str
    updated_at:str
    deleted_at:str
