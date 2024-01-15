from fastapi import APIRouter, Depends, HTTPException
from ...services import booking_service, security_service
from ... import schemas, database
from sqlalchemy.orm import Session
from pydantic import ValidationError

router = APIRouter(prefix="/bookings" , tags=["Bookings"])

@router.post("/", response_model=schemas.Booking)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    try:
        return booking_service.create_booking(db, booking)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

@router.put("/{id}", response_model=schemas.Booking)
def update_booking(id: int, booking: schemas.BookingUpdate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    booking = booking_service.update_booking(db, id, booking)
    return booking

@router.get("/", response_model=schemas.BookingList)
def get_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    bookings, total = booking_service.get_bookings(db, skip, limit)
    return {"items": bookings, "total": total}

@router.get("/{id}", response_model=schemas.Booking)
def get_booking(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    booking = booking_service.get_booking(db, id)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.delete("/{id}")
def delete_booking(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    return booking_service.delete_booking(db, id)
