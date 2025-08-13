from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.menu import MenuItem

router = APIRouter(prefix="/menu", tags=["Menu"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

  
