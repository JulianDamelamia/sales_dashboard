from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
import datetime
import numpy as np

from db.models import Base, Distributor, Region, Employees, Product, Sales

faker = Faker("es_AR")
random.seed(42)
np.random.seed(42)

DATABASE_URL = "postgresql+psycopg2://bi_user:1234@localhost:5432/sales_db"

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
session = Session()


# Crear tablas
Base.metadata.drop_all(engine)  # Opcional: limpiar todo antes
Base.metadata.create_all(engine)

# ---------- Generación de datos ---------- #
def populate_database():
    # info para datos sintéticos
    ciudades_arg = [
        ("Córdoba", "Córdoba"),
        ("Rosario", "Santa Fe"),
        ("Mendoza", "Mendoza"),
        ("San Miguel de Tucumán", "Tucumán"),
        ("CABA", "CABA"),
        ("La Plata", "Buenos Aires"),
        ("Mar del Plata", "Buenos Aires"),
        ("Salta", "Salta"),
        ("Neuquén", "Neuquén"),
        ("San Juan", "San Juan"),
        ("Posadas", "Misiones"),
    ]
    categorias = ["Electrónica", "Alimentos", "Bebidas", "Ropa", "Hogar"]

    ## Distributors
    distribuidores = [Distributor(name=f"Distribuidor {i}") for i in range(1, 6)]
    session.add_all(distribuidores)
    session.commit()

    # Regions
    regiones = []
    for ciudad, provincia in ciudades_arg:
        regiones.append(Region(city=ciudad, province=provincia))
    session.add_all(regiones)
    session.commit()

    # Employees
    empleados = []
    for _ in range(20):
        empleado = Employees(
            name=faker.name(),
            distributor_id=random.choice(distribuidores).id,
            region_id=random.choice(regiones).id
        )
        empleados.append(empleado)
    session.add_all(empleados)
    session.commit()

    # Products
    productos = []
    for _ in range(15):
        productos.append(Product(
            name=faker.word().capitalize(),
            category=random.choice(categorias)
        ))
    session.add_all(productos)
    session.commit()

    # ---------- Carga de hechos (ventas) ---------- #

    ventas = []
    fecha_inicio = datetime.date(2024, 1, 1)
    for _ in range(2000):
        ventas.append(Sales(
            date=fecha_inicio + datetime.timedelta(days=random.randint(0, 180)),
            quantity=random.randint(1, 10),
            price=round(random.uniform(5, 100), 2),
            employee_id=random.choice(empleados).id,
            product_id=random.choice(productos).id
        ))
    session.add_all(ventas)
    session.commit()

    print("📦 Base de datos poblada con éxito.")