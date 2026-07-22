

from http.client import HTTPException
from subprocess import DETACHED_PROCESS

from app.crud.trip import get_trip_by_id, get_user_trips


def list_trips(db, current_user):
    return get_user_trips(db, current_user.user_id)

def get_trip(db, current_user, trip_id: int):
    trip = get_trip_by_id(db, trip_id)

    if not  trip:
        raise HTTPException(
            status_code=404,
            detail="Trip Not Found"
        )

    if trip.user_id != current_user.user_id:
        raise HTTPException(
            status_code= 403,
            detail="Not authorized"
        )

    return trip