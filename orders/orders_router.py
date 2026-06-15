import asyncio
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.products.models import Product
from app.orders.models import Order
from app.orders.schemas import OrderCreate, OrderResponse

router = APIRouter(prefix="/orders", tags=["Orders"])

async def send_sms_notification(order_id: int):
    print(f"[BG TASK] Initiating SMS delivery for order #{order_id}...")
    await asyncio.sleep(3.0)
    print(f"[BG TASK] SMS successfully sent to the customer for order #{order_id}!")

@router.post("/", response_model=OrderResponse)
def create_order(
    payload: OrderCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == payload.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.stock < payload.quantity:
        raise HTTPException(status_code=400, detail="Out of stock")

    product.stock -= payload.quantity
    total_price = product.price_usd * payload.quantity

    new_order = Order(
        product_id=payload.product_id,
        quantity=payload.quantity,
        total_price_usd=total_price,
        status="completed"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    background_tasks.add_task(send_sms_notification, new_order.id)

    return new_order