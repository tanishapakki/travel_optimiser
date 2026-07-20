import pytest
from unittest.mock import patch

from app.graph.planner_graph import planner_graph
from app.schemas.itinerary import Itinerary


@pytest.mark.parametrize(
    "duration_days,budget",
    [
        (1, 500),
        (3, 1500),
        (7, 5000),
    ],
)
def test_itinerary_day_count_matches_duration(
    duration_days,
    budget,
):
    itinerary_days = []

    for day_number in range(1, duration_days + 1):
        itinerary_days.append(
            {
                "day_number": day_number,
                "date": f"2026-08-{9 + day_number:02d}",
                "notes": f"Day {day_number}",
                "itinerary_items": [
                    {
                        "category_id": 1,
                        "item_type": "activity",
                        "title": "Explore destination",
                        "location": "Paris",
                        "estimated_cost": 50.0,
                        "notes": "Sightseeing",
                    }
                ],
            }
        )

    mock_itinerary = Itinerary(
        itinerary_days=itinerary_days
    )
    
    trip_input = {
        "start_location": "Mumbai",
        "destination": "Paris",
        "start_date": "2026-08-10",
        "end_date":"2026-09-10",
        "days": duration_days ,
        "travellers":2,
    }

    with patch(
        "app.graph.planner_graph.generate_structured",
        return_value=mock_itinerary,
    ):
        result = planner_graph.invoke(
            {
                "trip_input": trip_input,
            }
        )

    assert len(
        result["itinerary"].itinerary_days
    ) == duration_days