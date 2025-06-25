rom sqlalchemy import func
from db.models import Sales

def total_ventas(session):
    total = session.query(func.sum(Sales.quantity * Sales.unit_price)).scalar()
    return round(total or 0, 2)