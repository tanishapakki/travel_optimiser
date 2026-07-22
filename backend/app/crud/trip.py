from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from app.models.trip import Trip
from app.models.itineraryitems import ItineraryItem
from app.models.itinerarydays import ItineraryDays

def get_user_trips(db:Session, user_id:int):
    trips= (
        db.query(Trip)
        .filter(Trip.user_id == user_id)
        .all()
    )

    result =[]

    for trip in trips:
        day_count = (
            db.query(func.count(ItineraryDays.day_id))
            .filter(ItineraryDays.trip_id == trips.trip_id)
            .scalar()
        )

        total_cost = (
            db.query(func.coalesce(func.sum(ItineraryItem.cost),0))
            .join(ItineraryDays, ItineraryItem.day_id ==ItineraryDays.day_id)
            .filter(ItineraryDays.trip_id == trips.trip_id)
            .scalar()
        )


        result.append(
            {
                "trip": trips,
                "day_count": day_count,
                "total_cost": total_cost
            }
        )
    return result


def get_trip_by_id(db: Session, trip_id:int):
    return(
        db.query(Trip)
        .options(
            joinedload(Trip.itinerary_days)
            .joinedload(ItineraryDays.itinerary_items)
        )
        .filter(Trip.trip_id == trip_id)
        .first()
    )