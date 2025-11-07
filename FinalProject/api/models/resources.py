from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..dependencies.database import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item = Column(String(100), unique=True, nullable=False)
    current_amount = Column(Float, nullable=False, server_default='0.0')
    unit = Column(String(20))
    reorder_level = Column(Float, server_default='0.0')
    last_updated = Column(DateTime, server_default=func.now())

    recipes = relationship("Recipe", back_populates="resource")