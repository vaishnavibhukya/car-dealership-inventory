from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.database import get_db
from app.models.car import Car

router = APIRouter()


@router.get("/stats")
def get_dashboard_stats(
    db: Session = Depends(get_db)
):
    total_cars = db.query(func.sum(Car.quantity)).scalar() or 0

    available_cars = (
        db.query(func.sum(Car.quantity))
        .filter(Car.status == "available")
        .scalar()
        or 0
    )

    sold_cars = (
        db.query(func.sum(Car.quantity))
        .filter(Car.status == "sold")
        .scalar()
        or 0
    )

    total_inventory_value = (
        db.query(func.sum(Car.price * Car.quantity)).scalar()
        or 0
    )

    return {
        "total_cars": total_cars,
        "available_cars": available_cars,
        "sold_cars": sold_cars,
        "total_inventory_value": total_inventory_value
    }