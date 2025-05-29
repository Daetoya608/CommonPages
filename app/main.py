from fastapi import FastAPI
from contextlib import asynccontextmanager
from .routes import router
from .database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield

app = FastAPI(
    title="CommonPages",
    lifespan=lifespan,
)

app.include_router(router, tags=["CommonPages"])
