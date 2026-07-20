

from datetime import datetime

from pydantic import BaseModel


class TripInput(BaseModel):
    destination: str
    days: int
    start_location:str
    travellers:int
    start_date: datetime
    end_date: datetime
