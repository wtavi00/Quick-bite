from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderOut 

router = APIRouter(prefix="/orders", tags=["Orders"])

