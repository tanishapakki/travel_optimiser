


from sqlalchemy import  Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.base import BaseModel


class Feedback(BaseModel):
    __tablename__ = "feedback"

    feedback_id = Column(Integer, primary_key=True, index=True,  nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    trip_id = Column(Integer, ForeignKey("trips.trip_id"), nullable=False)
    item_id = Column(Integer, ForeignKey("itineraryitems.item_id"), nullable=False)
    rating = Column(Integer, nullable=False)

    user = relationship("User", back_populates="feedback")

    trip = relationship("Trip", back_populates="feedback")

    itinerary_item = relationship(
        "ItineraryItem",
        back_populates="feedback"
    )