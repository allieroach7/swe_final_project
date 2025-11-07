from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    category = Column(String(50))
    calories = Column(Integer)
    ingredients = Column(Text)
    is_available = Column(Integer, default=1)

    order_details = relationship("OrderDetail", back_populates="menu_item")
    recipes = relationship("Recipe", back_populates="menu_item")