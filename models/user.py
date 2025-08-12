from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
  
