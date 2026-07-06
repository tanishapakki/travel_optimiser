


from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship
from app.base import BaseModel


class Feedback(BaseModel):
    __tablename__ = "feedback"

    feedback_id = Column(Integer, primary_key=True, index=True,  nullable=False)
    user_id = Column(Integer, nullable=False)
    trip_id = Column(Integer, nullable=False)
    item_id = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)

    user = relationship("User", back_populates="feedback")

    trip = relationship("Trip", back_populates="feedback")

    itinerary_item = relationship(
        "ItineraryItem",
        back_populates="feedback"
    )