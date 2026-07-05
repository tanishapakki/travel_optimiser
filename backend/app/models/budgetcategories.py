


from sqlalchemy import Decimal, Column, Integer, String
from sqlalchemy.orm import relationship
from backend.app.database import Base


class BudgetCategories(Base):
    __tablename__ = "budgetcategories"

    category_id = Column(Integer, primary_key=True, index=True,  nullable=False)
    trip_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    allocated_amount = Column(Decimal(10, 2), nullable=False)
    spent_amount = Column(Decimal(10, 2), nullable=False)
    currency = Column(String(5), nullable=False)

    trip = relationship("Trip", back_populates="budget_categories")

    itinerary_items = relationship(
        "ItineraryItem",
        back_populates="budgetcategories"
    )
