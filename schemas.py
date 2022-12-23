from typing import List, Optional
from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    title: str = Field(
        example="Samsung A10",
        alias="product",
        description="The product name",
        max_length=32,
        min_length=3,
        regex="[a-zA-Z0-9]+")
    description: Optional[str] = Field(
        example="A very smartphone by samsung",
        default=None,
        min_length=10,
        max_length=100,
    )
    price: float = Field(
        example=2000.00,
        gt=0,
    )

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str = Field(
        example="ousmaneleye2001@gmail.com",
        regex="[a-z0-9]+@[a-z]+\.[a-z]+"
    )
class UserCreate(UserBase):
    password: str = Field(
        min_length=8,
        max_length=32,
    )
class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    class Config:
        orm_mode = True