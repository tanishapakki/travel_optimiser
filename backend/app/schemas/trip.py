

from pydantic import BaseModel


class TripPlanSchema(BaseModel):
    destination: str
    days: int

    