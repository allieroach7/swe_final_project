from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .order_details import OrderDetail
from .payments import Payment

class OrderBase(BaseModel):
    customer_id: int
    total_price: float
    status: str = "pending"
    description: Optional[str] = None

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    status: Optional[str] = None
    total_price: Optional[float] = None
    description: Optional[str] = None

class Order(OrderBase):
    id: int
    order_date: datetime
    tracking_number: Optional[str] = None
    order_details: List[OrderDetail] = []
    payment: Optional[Payment] = None

    class ConfigDict:
        from_attributes = True