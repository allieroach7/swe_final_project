from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PaymentBase(BaseModel):
    amount: float
    payment_method: str
    status: str = "pending"

class PaymentCreate(PaymentBase):
    order_id: int

class PaymentUpdate(BaseModel):
    amount: Optional[float] = None
    payment_method: Optional[str] = None
    status: Optional[str] = None
    transaction_id: Optional[str] = None

class Payment(PaymentBase):
    id: int
    order_id: int
    transaction_id: Optional[str] = None
    payment_date: datetime

    class ConfigDict:
        from_attributes = True