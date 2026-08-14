from fastapi import FastAPI
from .database import engine, Base
from .routers import users, workouts
from . import models

# Create all database tables defined in models.py
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gym & Performance Progress Tracker API",
    description="A backend REST API built with FastAPI, SQLAlchemy, and JWT Authentication.",
    version="1.0.0",
)

# Include Modular Routers
app.include_router(users.router)
app.include_router(workouts.router)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Gym Progress API! Visit /docs for the interactive Swagger documentation."
    }