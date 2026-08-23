from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base


class Car(Base):
    __tablename__ = "cars"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    make = Column(
        String,
        nullable=False
    )

    model = Column(
        String,
        nullable=False
    )

    year = Column(
        Integer,
        nullable=False
    )

    price = Column(
        Float,
        nullable=False
    )

    mileage = Column(
        Integer,
        nullable=False
    )

    color = Column(
        String,
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False,
        default=1
    )

    status = Column(
        String,
        nullable=False,
        default="available"
    )