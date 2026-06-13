from sqlalchemy import Column, Integer, String, Float
from app.core.db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True, nullable=False)
    price_usd = Column(Float, nullable=False)
    stock = Column(Integer, default=0)