

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.app.base import BaseModel


class Trip(BaseModel):
    __tablename__ = "trips"

    trip_id = Column(Integer, primary_key=True, index=True,  nullable=False)
    user_id = Column(Integer, nullable=False)
    destination = Column(String(255), nullable=False)
    start_location = Column(String(100), nullable=False)
    travelers = Column(Integer, nullable=False)
    start_date = Column(String(100), nullable=False)
    end_date = Column(String(100), nullable=False)

    user = relationship("User", back_populates="trips")
    