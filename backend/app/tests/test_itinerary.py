from datetime import datetime

from app.schemas.itinerary import Itinerary


def test_itinerary_schema_instantiation():
    data = {
        "itinerary_days": [
            {
                "day_number": 1,
                "date": "2026-08-10",
                "notes": "Explore central Paris",
                "itinerary_items": [
                    {
                        "category_id": 1,
                        "item_type": "activity",
                        "title": "Visit Eiffel Tower",
                        "location": "Champ de Mars",
                        "start_time": "2026-08-10T09:00:00",
                        "end_time": "2026-08-10T11:00:00",
                        "source_agent": "planner",
                    }
                ],
            }
        ]
    }

    itinerary = Itinerary.model_validate(data)

    assert len(itinerary.itinerary_days) == 1

    day = itinerary.itinerary_days[0]

    assert day.day_number == 1
    assert day.date == "2026-08-10"
    assert day.notes == "Explore central Paris"

    assert len(day.itinerary_items) == 1

    item = day.itinerary_items[0]

    assert item.category_id == 1
    assert item.item_type == "activity"
    assert item.title == "Visit Eiffel Tower"
    assert item.location == "Champ de Mars"
    assert item.source_agent == "planner"

    assert isinstance(item.start_time, datetime)
    assert isinstance(item.end_time, datetime)