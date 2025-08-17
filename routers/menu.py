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

  
@router.post("/", response_model=MenuItemOut)
def create_item(item: MenuItemCreate, db: Session = Depends(get_db)):
    new_item = MenuItem(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@router.get("/", response_model=list[MenuItemOut])
def list_items(db: Session = Depends(get_db)):
    return db.query(MenuItem).all()
