from datetime import datetime

from pydantic import BaseModel, Field


class ItineraryItem(BaseModel):
    item_id: int | None = None
    day_id: int | None = None
    category_id: int

    item_type: str
    title: str | None = None
    location: str | None = None

    start_time: datetime | None = None
    end_time: datetime | None = None

    source_agent: str | None = None


class ItineraryDays(BaseModel):
    day_id: int | None = None
    trip_id: int | None = None

    day_number: int
    date: str
    notes: str | None = None

    itinerary_items: list[ItineraryItem] = Field(
        default_factory=list
    )


class Itinerary(BaseModel):
    itinerary_days: list[ItineraryDays] = Field(
        default_factory=list
    )