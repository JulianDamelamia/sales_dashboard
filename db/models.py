from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#dimension tables 

class Distributor(Base):
    __tablename__ = 'dim_distributor'
    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable=False)

    employees = relationship('Employees', back_populates='distributor')

class Region(Base):
    __tablename__ = 'dim_zone'
    id = Column(Integer, primary_key=True)
    city = Column(String(50), nullable=False)
    province = Column(String(50), nullable=False)

    employees = relationship('Employees', back_populates='region')

class Employees(Base):
    __tablename__ = 'dim_employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    distributor_id = Column(Integer, ForeignKey('dim_distributor.id'), nullable=False)
    region_id = Column(Integer, ForeignKey('dim_zone.id'), nullable=False)

    distributor = relationship('Distributor', back_populates='employees')
    region = relationship('Region', back_populates='employees')
    sales = relationship('Sales', back_populates='employee')

class Product(Base):
    __tablename__ = 'dim_product'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)

    sales = relationship('Sales', back_populates='product')

#Fact tables

class Sales(Base):
    __tablename__ = 'fact_sales'
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('dim_employee.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('dim_product.id'), nullable=False)
    date = Column(Date, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    employee = relationship('Employees', back_populates='sales')
    product = relationship('Product', back_populates='sales')