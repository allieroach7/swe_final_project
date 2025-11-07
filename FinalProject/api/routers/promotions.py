from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..dependencies.database import get_db
from ..models.promotions import Promotion as PromotionModel
from ..schemas.promotions import Promotion, PromotionCreate, PromotionUpdate

router = APIRouter()


@router.post("/promotions/", response_model=Promotion)
def create_promotion(promotion: PromotionCreate, db: Session = Depends(get_db)):
    db_promotion = PromotionModel(**promotion.dict())
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion


@router.get("/promotions/", response_model=List[Promotion])
def read_promotions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    promotions = db.query(PromotionModel).offset(skip).limit(limit).all()
    return promotions


@router.get("/promotions/{promotion_id}", response_model=Promotion)
def read_promotion(promotion_id: int, db: Session = Depends(get_db)):
    promotion = db.query(PromotionModel).filter(PromotionModel.id == promotion_id).first()
    if promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotion


@router.put("/promotions/{promotion_id}", response_model=Promotion)
def update_promotion(promotion_id: int, promotion: PromotionUpdate, db: Session = Depends(get_db)):
    db_promotion = db.query(PromotionModel).filter(PromotionModel.id == promotion_id).first()
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")

    for key, value in promotion.dict(exclude_unset=True).items():
        setattr(db_promotion, key, value)

    db.commit()
    db.refresh(db_promotion)
    return db_promotion