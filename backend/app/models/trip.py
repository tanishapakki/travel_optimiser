

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.base import BaseModel


class Trip(BaseModel):
    __tablename__ = "trips"

    trip_id = Column(Integer, primary_key=True, index=True,  nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    destination = Column(String(255), nullable=False)
    start_location = Column(String(100), nullable=False)
    travelers = Column(Integer, nullable=False)
    start_date = Column(String(100), nullable=False)
    end_date = Column(String(100), nullable=False)

    user = relationship("User", back_populates="trips")

    itinerary_days = relationship(
        "ItineraryDay",
        back_populates="trip",
        cascade="all, delete-orphan"
    )

    budget_categories = relationship(
        "BudgetCategory",
        back_populates="trip",
        cascade="all, delete-orphan"
    )

    preferences = relationship(
        "Preference",
        back_populates="trip",
        cascade="all, delete-orphan"
    )

    feedback = relationship(
        "Feedback",
        back_populates="trip",
        cascade="all, delete-orphan"
    )

    chat_messages = relationship(
        "ChatMessage",
        back_populates="trip",
        cascade="all, delete-orphan"
    )