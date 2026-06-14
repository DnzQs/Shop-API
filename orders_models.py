from sqlalchemy import Column, Integer, ForeignKey, Float, String
from app.core.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False)
    total_price_usd = Column(Float, nullable=False)
    status = Column(String(50), default="pending")