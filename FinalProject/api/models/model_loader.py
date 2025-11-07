from . import orders, order_details, menu_items, customers, payments, promotions, reviews
from ..dependencies.database import engine

def index():
    customers.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    payments.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)