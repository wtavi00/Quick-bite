from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderOut 

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrderOut)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = Order(user_id=1, item_ids=",".join(map(str, order.item_ids)))
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

