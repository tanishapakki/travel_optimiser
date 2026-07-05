

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from backend.app.database import Base



class ItineraryDay(Base):
    __tablename__ = "itinerary_days"

    day_id = Column(Integer, primary_key=True, index=True,  nullable=False)
    trip_id = Column(Integer, nullable=False)
    day_number = Column(Integer, nullable=False)
    date = Column(String(100), nullable=False)
    notes = Column(String, nullable=True)
    trip = relationship("Trip", back_populates="itinerary_days")

    itinerary_items = relationship(
        "ItineraryItem",
        back_populates="itinerary_day",
        cascade="all, delete-orphan"
    )
