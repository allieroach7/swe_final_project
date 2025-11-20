from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from ..dependencies.database import get_db
from ..models.customers import Customer as CustomerModel
from ..models.menu_items import MenuItem as MenuItemModel
from ..models.orders import Order as OrderModel
from ..models.reviews import Review as ReviewModel
from ..schemas.customers import CustomerCreate, Customer
from ..schemas.menu_items import MenuItem
from ..schemas.reviews import ReviewCreate, Review

router = APIRouter()

@router.post("/customers/register", response_model=Customer, tags=["Customer"])
def register_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    """
    Register a new customer with name, phone, and address for food delivery
    
    - **name**: Customer's full name
    - **email**: Customer's email address
    - **phone**: Customer's phone number for delivery updates
    - **address**: Delivery address including street, city, zip code
    """
    # Check if email already exists
    existing_customer = db.query(CustomerModel).filter(CustomerModel.email == customer.email).first()
    if existing_customer:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_customer = CustomerModel(
        name=customer.name,
        email=customer.email,
        phone=customer.phone,
        address=customer.address
    )
    
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

@router.get("/menu", response_model=Dict[str, List[MenuItem]], tags=["Customer"])
def browse_menu(db: Session = Depends(get_db)):
    """
    Browse the complete menu organized by categories
    
    Returns menu items grouped by category (appetizers, main courses, desserts, drinks, etc.)
    Only shows available items (is_available = 1)
    """
    menu_items = db.query(MenuItemModel).filter(MenuItemModel.is_available == 1).all()
    
    categories = {}
    for item in menu_items:
        if item.category not in categories:
            categories[item.category] = []
        categories[item.category].append(item)
    
    return categories

@router.get("/menu/category/{category_name}", response_model=List[MenuItem], tags=["Customer"])
def browse_menu_by_category(category_name: str, db: Session = Depends(get_db)):
    """
    Browse menu items by specific category
    
    - **category_name**: The category to filter by (e.g., 'main', 'appetizer', 'dessert', 'drink')
    """
    menu_items = db.query(MenuItemModel).filter(
        MenuItemModel.category == category_name,
        MenuItemModel.is_available == 1
    ).all()
    
    if not menu_items:
        raise HTTPException(status_code=404, detail=f"No items found in category '{category_name}'")
    
    return menu_items

@router.post("/reviews", response_model=Review, tags=["Customer"])
def submit_review(review: ReviewCreate, db: Session = Depends(get_db)):
    """
    Submit a rating and review for an order
    
    - **customer_id**: ID of the customer submitting the review
    - **order_id**: ID of the order being reviewed
    - **rating**: Rating from 1-5 stars
    - **review_text**: Detailed review comments (optional)
    """
    # Verify the order exists and belongs to the customer
    order = db.query(OrderModel).filter(
        OrderModel.id == review.order_id,
        OrderModel.customer_id == review.customer_id
    ).first()
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found or doesn't belong to customer")
    
    # Check if review already exists for this order
    existing_review = db.query(ReviewModel).filter(ReviewModel.order_id == review.order_id).first()
    if existing_review:
        raise HTTPException(status_code=400, detail="Review already submitted for this order")
    
    new_review = ReviewModel(
        customer_id=review.customer_id,
        order_id=review.order_id,
        rating=review.rating,
        review_text=review.review_text
    )
    
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review

@router.get("/reviews/customer/{customer_id}", response_model=List[Review], tags=["Customer"])
def get_customer_reviews(customer_id: int, db: Session = Depends(get_db)):
    """
    Get all reviews submitted by a specific customer
    """
    reviews = db.query(ReviewModel).filter(ReviewModel.customer_id == customer_id).all()
    return reviews

@router.get("/reviews/menu-item/{menu_item_id}", response_model=List[Dict[str, Any]], tags=["Customer"])
def get_reviews_for_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    """
    Get all reviews for a specific menu item
    
    Returns reviews with customer names for better context
    """
    reviews = db.query(ReviewModel, CustomerModel.name).join(
        CustomerModel, ReviewModel.customer_id == CustomerModel.id
    ).join(
        OrderModel, ReviewModel.order_id == OrderModel.id
    ).join(
        OrderModel.order_details
    ).filter(
        OrderModel.order_details.any(menu_item_id=menu_item_id)
    ).all()
    
    result = []
    for review, customer_name in reviews:
        result.append({
            "id": review.id,
            "customer_name": customer_name,
            "rating": review.rating,
            "review_text": review.review_text,
            "created_at": review.created_at
        })
    
    return result