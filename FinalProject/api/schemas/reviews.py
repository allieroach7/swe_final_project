from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ReviewBase(BaseModel):
    rating: int
    review_text: Optional[str] = None

class ReviewCreate(ReviewBase):
    customer_id: int
    order_id: int

class ReviewUpdate(BaseModel):
    rating: Optional[int] = None
    review_text: Optional[str] = None

class Review(ReviewBase):
    id: int
    customer_id: int
    order_id: int
    created_at: datetime

    class ConfigDict:
        from_attributes = True