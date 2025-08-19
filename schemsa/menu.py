from pydantic import BaseModel

class MenuItemCreate(BaseModel):
    name: str
    description: str
    price: float

class MenuItemOut(MenuItemCreate):
    id: int

    class Config:
        orm_mode = True

  
