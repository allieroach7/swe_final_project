from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ResourceBase(BaseModel):
    item: str
    current_amount: float
    unit: str
    reorder_level: Optional[float] = 0.0

class ResourceCreate(ResourceBase):
    pass

class ResourceUpdate(BaseModel):
    item: Optional[str] = None
    current_amount: Optional[float] = None
    unit: Optional[str] = None
    reorder_level: Optional[float] = None

class Resource(ResourceBase):
    id: int
    last_updated: datetime

    class ConfigDict:
        from_attributes = True