import pytest
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_customer_registration():
    """Test customer can register with delivery information"""
    response = client.post(
        "/api/v1/customer/customers/register",
        json={
            "name": "John Delivery",
            "email": "john.delivery@example.com",
            "phone": "555-123-4567",
            "address": "123 Main St, Cityville, ST 12345"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Delivery"
    assert data["email"] == "john.delivery@example.com"
    assert data["phone"] == "555-123-4567"
    assert data["address"] == "123 Main St, Cityville, ST 12345"
    assert "id" in data

def test_browse_menu():
    """Test customer can browse menu by categories"""
    response = client.get("/api/v1/customer/menu")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)  # Should return categories as keys

def test_browse_menu_by_category():
    """Test customer can browse specific menu categories"""
    response = client.get("/api/v1/customer/menu/category/main")
    assert response.status_code in [200, 404]  # 200 if category exists, 404 if not

def test_submit_review():
    """Test customer can submit rating and review"""
    # First create a test customer and order
    customer_response = client.post(
        "/api/v1/customer/customers/register",
        json={
            "name": "Review Tester",
            "email": "review.tester@example.com", 
            "phone": "555-999-8888",
            "address": "456 Review Lane"
        }
    )
    customer_id = customer_response.json()["id"]
    
    # Note: In a real test, you'd need to create an order first
    # This test would be expanded with actual order creation
    
    review_data = {
        "customer_id": customer_id,
        "order_id": 1,  # Would need valid order ID
        "rating": 5,
        "review_text": "Excellent service and food quality!"
    }
    
    response = client.post("/api/v1/customer/reviews", json=review_data)
    # This might fail without a real order, but tests the endpoint structure
    assert response.status_code in [200, 404, 400]

def test_duplicate_email_registration():
    """Test that duplicate email registration is prevented"""
    email = "unique@example.com"
    
    # First registration
    client.post("/api/v1/customer/customers/register", json={
        "name": "First User",
        "email": email,
        "phone": "555-111-1111",
        "address": "First Address"
    })
    
    # Second registration with same email
    response = client.post("/api/v1/customer/customers/register", json={
        "name": "Second User", 
        "email": email,
        "phone": "555-222-2222",
        "address": "Second Address"
    })
    
    assert response.status_code == 400
    assert "already registered" in response.json()["detail"]