from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))  # Fixed: references orders.id
    rating = Column(Integer, nullable=False)
    review_text = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

    customer = relationship("Customer", back_populates="reviews")
    order = relationship("Order", back_populates="review")