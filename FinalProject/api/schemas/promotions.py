from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PromotionBase(BaseModel):
    code: str
    description: Optional[str] = None
    discount_type: str
    discount_value: float
    expiration_date: Optional[datetime] = None

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    description: Optional[str] = None
    discount_type: Optional[str] = None
    discount_value: Optional[float] = None
    expiration_date: Optional[datetime] = None
    is_active: Optional[int] = None

class Promotion(PromotionBase):
    id: int
    is_active: int
    created_at: datetime

    class ConfigDict:
        from_attributes = True