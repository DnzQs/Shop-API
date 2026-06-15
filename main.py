from fastapi import FastAPI
from app.core.database import engine, Base
from app.products.router import router as products_router
from app.orders.router import router as orders_router
from app.products.models import Product
from app.orders.models import Order

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastShop Junior API",
    description="E-commerce API featuring async external API integration and background tasks",
    version="1.0.0"
)

app.include_router(products_router, prefix="/api/v1")
app.include_router(orders_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to Shop API! Go to /docs for Swagger documentation."}