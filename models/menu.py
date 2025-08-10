from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"
