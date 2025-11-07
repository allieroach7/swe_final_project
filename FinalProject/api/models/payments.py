from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))  # Fixed: references orders.id
    amount = Column(Float, nullable=False)
    payment_method = Column(String(50))
    status = Column(String(50), default="pending")
    transaction_id = Column(String(100))
    payment_date = Column(DateTime, server_default=func.now())

    order = relationship("Order", back_populates="payment")