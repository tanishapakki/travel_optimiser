
from sqlalchemy import Column, DateTime, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class ItineraryItem(Base):
    __tablename__ = "itinerary_items"

    item_id = Column(Integer, primary_key=True, index=True,  nullable=False)
    day_id = Column(Integer, ForeignKey("itinerary_days.day_id"), nullable=False)
    category_id = Column(Integer, ForeignKey("budgetcategories.category_id"), nullable=False)
    item_type = Column(String(20), nullable=False)
    title = Column(String(100), nullable=True)
    location = Column(String(100), nullable=True)

    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)

    source_agent = Column(String(50), nullable=True)

    itinerary_day = relationship(
        "ItineraryDays",
        back_populates="itinerary_items"
    )

    budgetcategories = relationship(
        "BudgetCategories",
        back_populates="itinerary_items"
    )

    feedback = relationship(
        "Feedback",
        back_populates="itinerary_item",
        cascade="all, delete-orphan"
    )