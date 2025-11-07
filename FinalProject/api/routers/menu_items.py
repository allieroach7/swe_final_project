from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..dependencies.database import get_db
from ..models.menu_items import MenuItem as MenuItemModel
from ..schemas.menu_items import MenuItem, MenuItemCreate, MenuItemUpdate

router = APIRouter()


@router.post("/menu-items/", response_model=MenuItem)
def create_menu_item(menu_item: MenuItemCreate, db: Session = Depends(get_db)):
    db_menu_item = MenuItemModel(**menu_item.dict())
    db.add(db_menu_item)
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item


@router.get("/menu-items/", response_model=List[MenuItem])
def read_menu_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    menu_items = db.query(MenuItemModel).offset(skip).limit(limit).all()
    return menu_items


@router.get("/menu-items/{menu_item_id}", response_model=MenuItem)
def read_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    menu_item = db.query(MenuItemModel).filter(MenuItemModel.id == menu_item_id).first()
    if menu_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return menu_item


@router.put("/menu-items/{menu_item_id}", response_model=MenuItem)
def update_menu_item(menu_item_id: int, menu_item: MenuItemUpdate, db: Session = Depends(get_db)):
    db_menu_item = db.query(MenuItemModel).filter(MenuItemModel.id == menu_item_id).first()
    if db_menu_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")

    for key, value in menu_item.dict(exclude_unset=True).items():
        setattr(db_menu_item, key, value)

    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item