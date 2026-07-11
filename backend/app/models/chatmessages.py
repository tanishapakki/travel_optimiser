

from sqlalchemy import DateTime, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.base import BaseModel


class ChatMessage(BaseModel):
    __tablename__ = "chatmessages"

    message_id = Column(Integer, primary_key=True, index=True,  nullable=False)
    trip_id = Column(Integer, ForeignKey("trips.trip_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    agent_name = Column(String(100))
    content = Column(String(200), nullable=False)

    user = relationship("User", back_populates="chat_messages")

    trip = relationship("Trip", back_populates="chat_messages")