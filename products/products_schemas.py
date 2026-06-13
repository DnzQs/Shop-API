from pydantic import BaseModel, ConfigDict
from typing import Optional

class ProductBase(BaseModel):
    title: str
    price_usd: float
    stock: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    converted_price: Optional[float] = None
    currency: str = "USD"

    model_config = ConfigDict(from_attributes=True)
