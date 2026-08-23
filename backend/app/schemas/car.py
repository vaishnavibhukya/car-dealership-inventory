from pydantic import BaseModel


class CarCreate(BaseModel):
    make: str
    model: str
    year: int
    price: float
    mileage: int
    color: str
    quantity: int = 1
    status: str = "available"


class CarResponse(BaseModel):
    id: int
    make: str
    model: str
    year: int
    price: float
    mileage: int
    color: str
    quantity: int
    status: str

    class Config:
        from_attributes = True