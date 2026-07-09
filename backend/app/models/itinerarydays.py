

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.db import Base



class ItineraryDays(Base):
    __tablename__ = "itinerary_days"

    day_id = Column(Integer, primary_key=True, index=True,  nullable=False)
    trip_id = Column(Integer, ForeignKey("trips.trip_id"), nullable=False)
    day_number = Column(Integer, nullable=False)
    date = Column(String(100), nullable=False)
    notes = Column(String, nullable=True)


    trip = relationship("Trip", back_populates="itinerary_days")

    itineraryitems = relationship(
        "ItineraryItem",
        back_populates="itinerarydays",
        cascade="all, delete-orphan"
    )
