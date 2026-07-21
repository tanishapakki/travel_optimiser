from datetime import date

from sqlalchemy import Column, Date, ForeignKey, Integer, Text, UniqueConstraint
from sqlalchemy.orm import relationship

from app.base import BaseModel


class ItineraryDays(BaseModel):
    __tablename__ = "itinerary_days"

    __table_args__ = (
        UniqueConstraint("trip_id", "day_number", name="uq_trip_day"),
    )

    day_id = Column(
        Integer,
        primary_key=True,
        index=True,
        nullable=False,
    )

    trip_id = Column(
        Integer,
        ForeignKey("trips.trip_id", ondelete="CASCADE"),
        nullable=False,
    )

    day_number = Column(
        Integer,
        nullable=False,
    )

    date = Column(
        Date,
        nullable=False,
    )

    notes = Column(
        Text,
        nullable=True,
    )

    trip = relationship(
        "Trip",
        back_populates="itinerary_days",
    )

    itinerary_items = relationship(
        "ItineraryItem",
        back_populates="itinerary_day",
        cascade="all, delete-orphan",
    )