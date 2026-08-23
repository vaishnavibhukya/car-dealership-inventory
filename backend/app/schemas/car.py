from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class CarCreate(BaseModel):
    make: str = Field(
        ...,
        min_length=1
    )

    model: str = Field(
        ...,
        min_length=1
    )

    year: int = Field(
        ...,
        ge=1900,
        le=2100
    )

    price: float = Field(
        ...,
        ge=0
    )

    mileage: int = Field(
        ...,
        ge=0
    )

    color: str = Field(
        ...,
        min_length=1
    )

    quantity: int = Field(
        default=1,
        ge=0
    )

    status: Literal[
        "available",
        "reserved",
        "sold"
    ] = "available"


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

    model_config = ConfigDict(
        from_attributes=True
    )