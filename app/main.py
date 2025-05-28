from fastapi import FastAPI
from routes import router
from database import create_tables

app = FastAPI(title="CommonPages")

app.include_router(router, tags=["CommonPages"])

@app.on_event("startup")
async def startup():
    await create_tables()
