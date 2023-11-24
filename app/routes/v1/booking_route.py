from fastapi import APIRouter, Depends, HTTPException
from ...services import booking_service
from ... import schemas, database
from sqlalchemy.orm import Session
from pydantic import ValidationError

router = APIRouter(prefix="/bookings" , tags=["Bookings"])

@router.post("/", response_model=schemas.Booking)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(database.get_db)):
    try:
        return booking_service.create_booking(db, booking)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

# TODO finir la route update_booking
@router.put("/{id}", response_model=schemas.Booking)
def update_booking(id: int, booking: schemas.BookingCreate, db: Session = Depends(database.get_db)):
    try:
        return booking_service.update_booking(db, id, booking)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

@router.get("/", response_model=schemas.BookingList)
def get_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    bookings, total = booking_service.get_bookings(db, skip, limit)
    return {"items": bookings, "total": total}

@router.get("/{id}", response_model=schemas.Booking)
def get_booking(id: int, db: Session = Depends(database.get_db)):
    booking = booking_service.get_booking(db, id)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.delete("/{id}")
def delete_booking(id: int, db: Session = Depends(database.get_db)):
    return booking_service.delete_booking(db, id)
