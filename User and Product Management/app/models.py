from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name:str
    email:str
    phone:Optional[str]=None
    address:Optional[str]=None


class Product(BaseModel):
    sku:int
    name:str
    price:float
    stock:int
    description:Optional[str]=None
