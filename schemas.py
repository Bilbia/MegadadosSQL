from typing import List, Optional

from pydantic import BaseModel


class DisciplinaBase(BaseModel):
    nome: str
    no


class DisciplinaCreate(ItemBase):
    
    pass


class (ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
