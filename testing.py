from sqlalchemy import func
from db.models import Sales
from db.populate_db import populate_database, session, engine
import pandas as pd



populate_database()
def total_ventas(session):
     total = session.query(func.sum(Sales.quantity * Sales.price)).scalar()
     return round(total or 0, 2)


df = pd.read_sql("SELECT * FROM dim_distributor", engine)

print(df.head())

print("Total ventas:", total_ventas(session))
#esto es una prueba para el bot de discord