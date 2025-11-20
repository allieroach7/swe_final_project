import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .dependencies.config import conf

from .models import model_loader

from .routers import index as indexRoute
from .routers import reviews, resources, users, customers  # added users and customers

app = FastAPI(
    title="Online Restaurant Ordering System API",
    description="""
    # Restaurant Ordering System API
    
    ## Customer Features:
    - 📝 **Register** - Create customer account with delivery information
    - 🍽️ **Browse Menu** - View available dishes organized by categories
    - ⭐ **Submit Reviews** - Rate and review your orders
    - 📦 **Track Orders** - Monitor order status and delivery progress
    
    ## Restaurant Staff Features:
    - 📊 **Analytics** - View popular items and revenue reports
    - 🛒 **Order Management** - Process and update orders
    - 📋 **Menu Management** - Manage menu items and availability
    - 💰 **Payment Processing** - Handle customer payments
    
    ## Quick Start:
    1. Register as a customer: `POST /api/v1/customer/customers/register`
    2. Browse the menu: `GET /api/v1/customer/menu`
    3. Place an order: `POST /api/v1/orders/`
    4. Submit review: `POST /api/v1/customer/reviews`
    """,
    version="1.0.0",
    contact={
        "name": "Restaurant Support",
        "email": "support@restaurant.com",
    },
    docs_url="/docs",
    redoc_url="/redoc"
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()

indexRoute.load_routes(app)

app.include_router(reviews.router)
app.include_router(resources.router)
app.include_router(users.router, prefix="/api", tags=["Users"])
app.include_router(customers.router, prefix="/api", tags=["Customers"])

@app.get("/", tags=["Documentation"])
def read_root():
    """
    # Welcome to Restaurant Ordering System API
    
    ## Available Documentation:
    - **Interactive Docs**: [/docs](/docs) - Test endpoints directly
    - **Alternative Docs**: [/redoc](/redoc) - Clean documentation view
    - **Health Check**: [/health](/health) - API status
    
    ## Key Customer Endpoints:
    - `POST /api/v1/customer/customers/register` - Register new customer
    - `GET /api/v1/customer/menu` - Browse full menu by categories
    - `GET /api/v1/customer/menu/category/{category}` - Browse by specific category
    - `POST /api/v1/customer/reviews` - Submit order review and rating
    - `GET /api/v1/customer/reviews/customer/{id}` - Get customer's reviews
    - `GET /api/v1/customer/reviews/menu-item/{id}` - Get reviews for menu item
    """
    return {
        "message": "Welcome to Online Restaurant Ordering System API",
        "documentation": {
            "swagger_ui": "/docs",
            "redoc": "/redoc",
            "health_check": "/health"
        },
        "customer_features": [
            "Register with delivery information",
            "Browse menu by categories", 
            "Submit ratings and reviews",
            "Track order status"
        ]
    }

@app.get("/health", tags=["Documentation"])
def health_check():
    """
    Health check endpoint to verify API is running
    """
    return {"status": "healthy", "service": "Restaurant Ordering API"}

if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)

