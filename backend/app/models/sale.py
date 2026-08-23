from datetime import datetime

from sqlalchemy import Column, Integer, Float, String, DateTime

from app.database.database import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    car_id = Column(
        Integer,
        nullable=False
    )

    car_name = Column(
        String,
        nullable=False
    )

    price = Column(
        Float,
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False,
        default=1
    )

    sold_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )