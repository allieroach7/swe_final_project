from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .customers import Base


class Promotion(Base):
    __tablename__ = "promotions"

    promo_id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False)
    description = Column(String(200))
    discount_type = Column(String(20))  # percentage, fixed
    discount_value = Column(Float, nullable=False)
    expiration_date = Column(DateTime)
    is_active = Column(Integer, default=1)  # 1 for active, 0 for inactive
    created_at = Column(DateTime(timezone=True), server_default=func.now())