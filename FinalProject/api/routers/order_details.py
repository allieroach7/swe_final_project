from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..dependencies.database import get_db
from ..models.order_details import OrderDetail as OrderDetailModel
from ..schemas.order_details import OrderDetail, OrderDetailCreate, OrderDetailUpdate

router = APIRouter()


@router.post("/order-details/", response_model=OrderDetail)
def create_order_detail(order_detail: OrderDetailCreate, db: Session = Depends(get_db)):
    db_order_detail = OrderDetailModel(**order_detail.dict())
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail


@router.get("/order-details/", response_model=List[OrderDetail])
def read_order_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    order_details = db.query(OrderDetailModel).offset(skip).limit(limit).all()
    return order_details


@router.get("/order-details/{order_detail_id}", response_model=OrderDetail)
def read_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    order_detail = db.query(OrderDetailModel).filter(OrderDetailModel.id == order_detail_id).first()
    if order_detail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return order_detail


@router.put("/order-details/{order_detail_id}", response_model=OrderDetail)
def update_order_detail(order_detail_id: int, order_detail: OrderDetailUpdate, db: Session = Depends(get_db)):
    db_order_detail = db.query(OrderDetailModel).filter(OrderDetailModel.id == order_detail_id).first()
    if db_order_detail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")

    for key, value in order_detail.dict(exclude_unset=True).items():
        setattr(db_order_detail, key, value)

    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail