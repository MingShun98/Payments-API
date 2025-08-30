# app/main.py
from fastapi import FastAPI
from app.db.db import Base, engine
from app.routers import todos

Base.metadata.create_all(bind=engine)
app = FastAPI(title='Todo API')  # <-- must be named *app* at module top-level
app.include_router(todos.router, prefix='/api/v1')


@app.get("/")
def root(): 
    return {"message": "Welcome to the start of software engineering."}

