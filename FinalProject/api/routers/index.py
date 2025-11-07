from . import customers, menu_items, orders, order_details, payments, promotions, reviews

def load_routes(app):
    # Include all your routers
    app.include_router(customers.router, prefix="/api/v1", tags=["customers"])
    app.include_router(menu_items.router, prefix="/api/v1", tags=["menu_items"])
    app.include_router(orders.router, prefix="/api/v1", tags=["orders"])
    app.include_router(order_details.router, prefix="/api/v1", tags=["order_details"])
    app.include_router(payments.router, prefix="/api/v1", tags=["payments"])
    app.include_router(promotions.router, prefix="/api/v1", tags=["promotions"])
    app.include_router(reviews.router, prefix="/api/v1", tags=["reviews"])