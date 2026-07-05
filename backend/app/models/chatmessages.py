


from sqlalchemy import DateTime, Decimal, Column, Integer, String
from sqlalchemy.orm import relationship
from backend.app.base import BaseModel


class ChatMessages(BaseModel):
    __tablename__ = "chatmessages"

    message_id = Column(Integer, primary_key=True, index=True,  nullable=False)
    trip_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    agent_name = Column(String(100))
    content = Column(String(200), nullable=False)
    
    user = relationship("User", back_populates="chat_messages")

    trip = relationship("Trip", back_populates="chat_messages")