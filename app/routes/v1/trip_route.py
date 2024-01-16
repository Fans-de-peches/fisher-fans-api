from fastapi import APIRouter, Depends, HTTPException
from ...services import trip_service, booking_service, security_service
from ... import schemas, database
from sqlalchemy.orm import Session
from pydantic import ValidationError

router = APIRouter(prefix="/trips" , tags=["Trips"])

@router.post("/", response_model=schemas.Trip)
def create_trip(trip: schemas.TripCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    try:
        return trip_service.create_trip(db, trip)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

@router.put("/{id}", response_model=schemas.Trip)
def update_trip(id: int, trip: schemas.TripUpdate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    trip = trip_service.update_trip(db, id, trip)
    return trip

@router.get("/", response_model=schemas.TripList)
def get_trips(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    trips, total = trip_service.get_trips(db, skip, limit)
    return {"items": trips, "total": total}

@router.get("/{id}", response_model=schemas.Trip)
def get_trip(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    trip = trip_service.get_trip(db, id)
    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip

@router.delete("/{id}")
def delete_trip(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    return trip_service.delete_trip(db, id)

# Routes about trip items lists

@router.get("/{id}/bookings", response_model=schemas.BookingList)
async def read_trip_bookings(id: int,db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    bookings, total = booking_service.get_trip_bookings(db, id)
    return {"items": bookings, "total": total}