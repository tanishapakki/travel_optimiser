from typing import Any, TypedDict

from app.schemas.itinerary import Itinerary
from app.schemas.trip import TripInput


class PlannerState(TypedDict, total=False):
    trip_input: TripInput

    itinerary: Itinerary
    
    validation_errors: list[str]

    repair_attempts: int

    output: Itinerary