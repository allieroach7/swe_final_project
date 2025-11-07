from typing import Optional
from pydantic import BaseModel
from .resources import Resource
from .menu_items import MenuItem

class RecipeBase(BaseModel):
    ingredient_name: str
    amount: float
    unit: str

class RecipeCreate(RecipeBase):
    menu_item_id: int
    resource_id: int

class RecipeUpdate(BaseModel):
    menu_item_id: Optional[int] = None
    resource_id: Optional[int] = None
    ingredient_name: Optional[str] = None
    amount: Optional[float] = None
    unit: Optional[str] = None

class Recipe(RecipeBase):
    id: int
    menu_item: Optional[MenuItem] = None
    resource: Optional[Resource] = None

    class ConfigDict:
        from_attributes = True