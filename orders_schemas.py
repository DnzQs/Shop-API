from pydantic import BaseModel, ConfigDict

class OrderCreate(BaseModel):
    product_id: int
    quantity: int

class OrderResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    total_price_usd: float
    status: str
    model_config = ConfigDict(from_attributes=True)