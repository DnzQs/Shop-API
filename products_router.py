from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
import httpx

from app.core.database import get_db
from app.products.products_models import Product
from app.products.products_schemas import ProductCreate, ProductResponse

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.get("/", response_model=list[ProductResponse])
async def get_products(
        currency: str = Query("USD", description="Валюта для отображения: USD, EUR или RUB"),
        db: Session = Depends(get_db)
):
    products = db.query(Product).all()

    if currency.upper() == "USD":
        return products

    url = f"https://open.er-api.com/v6/latest/USD"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=5.0)
            response.raise_for_status()
            data = response.json()
        except (httpx.HTTPError, KeyError):
            raise HTTPException(status_code=503, detail="Внешний сервис курсов валют недоступен")

    rates = data.get("rates", {})
    target_rate = rates.get(currency.upper())

    if not target_rate:
        raise HTTPException(status_code=400, detail=f"Валюта {currency} не поддерживается")

    response_products = []
    for p in products:
        p_data = ProductResponse.model_validate(p).model_dump()
        p_data["converted_price"] = round(p.price_usd * target_rate, 2)
        p_data["currency"] = currency.upper()
        response_products.append(p_data)

    return response_products