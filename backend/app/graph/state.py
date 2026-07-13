from typing import Any, TypedDict

from app.schemas.itinerary import Itinerary


class PlannerState(TypedDict, total=False):
    trip_input: dict[str, Any]

    draft_itinerary: Itinerary

    validation_errors: list[str]

    repair_attempts: int

    output: Itinerary