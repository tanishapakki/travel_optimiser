

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True,  nullable=False)
    name = Column(String(100), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    trips = relationship("Trip", back_populates="user", cascade="all, delete-orphan")

    preferences = relationship("Preference",back_populates="user",cascade="all, delete-orphan")

    feedback = relationship("Feedback",back_populates="user",cascade="all, delete-orphan" )

    chat_messages = relationship( "ChatMessage", back_populates="user",cascade="all, delete-orphan" )
    