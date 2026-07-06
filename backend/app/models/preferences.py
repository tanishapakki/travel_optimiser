
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Preference(Base):
    __tablename__ = "preferences"

    pref_id = Column(Integer, primary_key=True, index=True,  nullable=False)
    user_id = Column(Integer, nullable=False)
    trip_id = Column(Integer, nullable=False)
    pref_type = Column(String(100), nullable=False)
    pref_value = Column(String(255), nullable=False)

    user = relationship("User", back_populates="preferences")
    trip = relationship("Trip", back_populates="preferences")
