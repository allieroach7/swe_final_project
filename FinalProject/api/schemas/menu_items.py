from typing import Optional
from pydantic import BaseModel

class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category: Optional[str] = None
    calories: Optional[int] = None
    ingredients: Optional[str] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    calories: Optional[int] = None
    ingredients: Optional[str] = None
    is_available: Optional[int] = None

class MenuItem(MenuItemBase):
    id: int
    is_available: int

    class ConfigDict:
        from_attributes = True