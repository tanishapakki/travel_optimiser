

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.app.base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True,  nullable=False)
    name = Column(String(100), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hashed = Column(String(255), nullable=False)

    trips = relationship( "Trip", back_populates="user")
    preferences = relationship( "Preference", back_populates="user")
    