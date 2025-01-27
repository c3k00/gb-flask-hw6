import uvicorn
from users_routers import user_router
from items_routers import item_router
from orders_routers import order_router
from fastapi import FastAPI
from contextlib import asynccontextmanager
from db import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(user_router, tags=["users"])
app.include_router(item_router, tags=["items"])
app.include_router(order_router, tags=["orders"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)