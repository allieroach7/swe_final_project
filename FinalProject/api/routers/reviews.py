from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..controllers import reviews as review_ctrl
from ..schemas.reviews import Review, ReviewCreate, ReviewUpdate
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"]
)

@router.post("/", response_model=Review)
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    return review_ctrl.create(db, review)

@router.get("/", response_model=List[Review])
def read_reviews(db: Session = Depends(get_db)):
    return review_ctrl.read_all(db)

@router.get("/{review_id}", response_model=Review)
def read_review(review_id: int, db: Session = Depends(get_db)):
    return review_ctrl.read_one(db, review_id)

@router.put("/{review_id}", response_model=Review)
def update_review(review_id: int, review: ReviewUpdate, db: Session = Depends(get_db)):
    return review_ctrl.update(db, review_id, review)

@router.delete("/{review_id}")
def delete_review(review_id: int, db: Session = Depends(get_db)):
    return review_ctrl.delete(db, review_id)
