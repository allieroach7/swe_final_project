from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..dependencies.database import get_db
from ..models.reviews import Review as ReviewModel
from ..schemas.reviews import Review, ReviewCreate, ReviewUpdate

router = APIRouter()


@router.post("/reviews/", response_model=Review)
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    db_review = ReviewModel(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


@router.get("/reviews/", response_model=List[Review])
def read_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reviews = db.query(ReviewModel).offset(skip).limit(limit).all()
    return reviews


@router.get("/reviews/{review_id}", response_model=Review)
def read_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
    if review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return review


@router.put("/reviews/{review_id}", response_model=Review)
def update_review(review_id: int, review: ReviewUpdate, db: Session = Depends(get_db)):
    db_review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")

    for key, value in review.dict(exclude_unset=True).items():
        setattr(db_review, key, value)

    db.commit()
    db.refresh(db_review)
    return db_review