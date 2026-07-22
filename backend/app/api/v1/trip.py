

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.security import get_current_user
from app.services.trip import get_trip, list_trips

router= APIRouter(prefix="/trips", tags=["Trips"])

@router.get("")
def get_trips(
    db: Session = Depends(get_db),
    current_user= Depends(get_current_user)
):
    trips = list_trips(db, current_user)

    response =[]

    for t in trips:
        trip = t["trip"]

        response.append(
            {
                "trip_id": trip.trip_id,
                "destination": trip.destination,
                "start_date":trip.start_date,
                "end_date":trip.end_date,
                "day_count":t["day_count"],
                "total_cost": t["total_cost"],
            }
        )

    return response

@router.get("/{trip_id}")
def get_trip_details(
    trip_id:int,
    db: Session = Depends(get_db),
    current_user= Depends(get_current_user)
):
    return get_trip(db, current_user,trip_id)
    