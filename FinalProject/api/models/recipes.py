from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))
    ingredient_name = Column(String(100))
    amount = Column(Float, nullable=False, server_default='0.0')
    unit = Column(String(20))  # grams, ml, pieces, etc.

    menu_item = relationship("MenuItem", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")