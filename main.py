from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes import user, menu, order

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Quickbite")

# Include route modules
app.include_router(user.router)
app.include_router(menu.router)
app.include_router(order.router)
