

from datetime import datetime
from typing import List

from pydantic import BaseModel


class TripInput(BaseModel):
    destination: str
    days: int
    start_location:str
    travellers:int
    start_date: datetime
    end_date: datetime

class TripSummary(BaseModel):
    trip_id:int
    destination:str
    start_date:datetime|None
    end_date:datetime|None
    day_count: int
    total_cost:float

    class Config:
        from_attributes=True

class ItineraryItemResponse(BaseModel):
    item_id:int
    title: str
    start_time: datetime
    end_time:datetime
    cost:float|None

    class Config:
        from_attributes=True

class ItineraryDayResponse(BaseModel):
    day_id:int
    day_number: int
    items: List[ItineraryItemResponse]

    class Config:
        from_attributes=True

class TripResponse(BaseModel):
    trip_id:int
    destination: str
    start_date: datetime | None
    end_date: datetime | None 
    days: List[ItineraryDayResponse]

    class Config: 
        from_attributes= True

