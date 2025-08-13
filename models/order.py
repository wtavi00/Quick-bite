from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    item_ids = Column(String)  # Comma-separated item IDs
    status = Column(String, default="placed")


