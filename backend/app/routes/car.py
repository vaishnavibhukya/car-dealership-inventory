from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.car import Car
from app.schemas.car import CarCreate, CarResponse


router = APIRouter()


# ============================================================
# GET ALL CARS
# ============================================================

@router.get(
    "/",
    response_model=list[CarResponse]
)
def get_cars(
    make: str | None = None,
    status: str | None = None,
    color: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    if skip < 0:
        raise HTTPException(
            status_code=400,
            detail="skip cannot be negative"
        )

    if limit < 1 or limit > 100:
        raise HTTPException(
            status_code=400,
            detail="limit must be between 1 and 100"
        )

    query = db.query(Car)

    # Filter by make
    if make:
        query = query.filter(
            Car.make.ilike(f"%{make}%")
        )

    # Filter by status
    if status:
        query = query.filter(
            Car.status == status
        )

    # Filter by color
    if color:
        query = query.filter(
            Car.color.ilike(f"%{color}%")
        )

    # Minimum price
    if min_price is not None:
        query = query.filter(
            Car.price >= min_price
        )

    # Maximum price
    if max_price is not None:
        query = query.filter(
            Car.price <= max_price
        )

    cars = (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )

    return cars


# ============================================================
# GET SINGLE CAR
# ============================================================

@router.get(
    "/{car_id}",
    response_model=CarResponse
)
def get_car(
    car_id: int,
    db: Session = Depends(get_db)
):

    car = (
        db.query(Car)
        .filter(Car.id == car_id)
        .first()
    )

    if car is None:
        raise HTTPException(
            status_code=404,
            detail="Car not found"
        )

    return car


# ============================================================
# CREATE CAR
# ============================================================

@router.post(
    "/",
    response_model=CarResponse,
    status_code=201
)
def create_car(
    car: CarCreate,
    db: Session = Depends(get_db)
):

    # Quantity must be at least 1
    if car.quantity < 1:
        raise HTTPException(
            status_code=400,
            detail="Quantity must be at least 1"
        )

    # Price cannot be negative
    if car.price < 0:
        raise HTTPException(
            status_code=400,
            detail="Price cannot be negative"
        )

    # Mileage cannot be negative
    if car.mileage < 0:
        raise HTTPException(
            status_code=400,
            detail="Mileage cannot be negative"
        )

    # Create new car
    new_car = Car(
        make=car.make,
        model=car.model,
        year=car.year,
        price=car.price,
        mileage=car.mileage,
        color=car.color,
        quantity=car.quantity,
        status="available"
    )

    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    return new_car


# ============================================================
# UPDATE CAR
# ============================================================

@router.put(
    "/{car_id}",
    response_model=CarResponse
)
def update_car(
    car_id: int,
    car_data: CarCreate,
    db: Session = Depends(get_db)
):

    car = (
        db.query(Car)
        .filter(Car.id == car_id)
        .first()
    )

    if car is None:
        raise HTTPException(
            status_code=404,
            detail="Car not found"
        )

    if car_data.quantity < 0:
        raise HTTPException(
            status_code=400,
            detail="Quantity cannot be negative"
        )

    if car_data.price < 0:
        raise HTTPException(
            status_code=400,
            detail="Price cannot be negative"
        )

    if car_data.mileage < 0:
        raise HTTPException(
            status_code=400,
            detail="Mileage cannot be negative"
        )

    car.make = car_data.make
    car.model = car_data.model
    car.year = car_data.year
    car.price = car_data.price
    car.mileage = car_data.mileage
    car.color = car_data.color
    car.quantity = car_data.quantity

    # Automatically determine status
    if car.quantity == 0:
        car.status = "sold"
    else:
        car.status = "available"

    db.commit()
    db.refresh(car)

    return car


# ============================================================
# DELETE CAR
# ============================================================

@router.delete("/{car_id}")
def delete_car(
    car_id: int,
    db: Session = Depends(get_db)
):

    car = (
        db.query(Car)
        .filter(Car.id == car_id)
        .first()
    )

    if car is None:
        raise HTTPException(
            status_code=404,
            detail="Car not found"
        )

    db.delete(car)
    db.commit()

    return {
        "message": "Car deleted successfully"
    }


# ============================================================
# PURCHASE CAR
# ============================================================

@router.post(
    "/{car_id}/purchase",
    response_model=CarResponse
)
def purchase_car(
    car_id: int,
    db: Session = Depends(get_db)
):

    car = (
        db.query(Car)
        .filter(Car.id == car_id)
        .first()
    )

    if car is None:
        raise HTTPException(
            status_code=404,
            detail="Car not found"
        )

    # Cannot purchase if no stock
    if car.quantity <= 0:
        raise HTTPException(
            status_code=400,
            detail="Car is out of stock"
        )

    # Reduce quantity by 1
    car.quantity -= 1

    # If no cars are left, mark as sold
    if car.quantity == 0:
        car.status = "sold"
    else:
        car.status = "available"

    db.commit()
    db.refresh(car)

    return car


# ============================================================
# RESTOCK CAR
# ============================================================

@router.post(
    "/{car_id}/restock",
    response_model=CarResponse
)
def restock_car(
    car_id: int,
    db: Session = Depends(get_db)
):

    car = (
        db.query(Car)
        .filter(Car.id == car_id)
        .first()
    )

    if car is None:
        raise HTTPException(
            status_code=404,
            detail="Car not found"
        )

    # Increase stock by 1
    car.quantity += 1

    # Once restocked, it becomes available
    car.status = "available"

    db.commit()
    db.refresh(car)

    return car