from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine

from app.models.user import User
from app.models.car import Car

from app.routes import auth
from app.routes import car
from app.routes import dashboard


app = FastAPI(
    title="Car Dealership Inventory API",
    version="1.0.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# DATABASE TABLES
# ============================================================

Base.metadata.create_all(bind=engine)


# ============================================================
# AUTHENTICATION ROUTES
# ============================================================

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)


# ============================================================
# CAR ROUTES
# ============================================================

app.include_router(
    car.router,
    prefix="/cars",
    tags=["Cars"]
)


# ============================================================
# DASHBOARD ROUTES
# ============================================================

app.include_router(
    dashboard.router,
    prefix="/dashboard",
    tags=["Dashboard"]
)


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():
    return {
        "message": "Car Dealership Inventory API is running"
    }