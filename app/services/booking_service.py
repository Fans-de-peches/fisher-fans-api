from sqlalchemy.orm import Session
from .. import models, schemas
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from datetime import datetime

def create_booking(db: Session, booking: schemas.BookingCreate):
    try:
        booking_data = booking.model_dump()
        user = db.query(models.User).filter(models.User.user_id == booking.owner_id).first()
        trip = db.query(models.Trip).filter(models.Trip.trip_id == booking.trip_id).first()
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        if not trip:
            raise HTTPException(status_code=404, detail="Trip not found")
        
        if booking_data.get("date"):
            booking_data["date"] = datetime.strptime(booking_data["date"], "%Y-%m-%d").date()
        
        db_booking = models.Booking(**booking_data)
        db.add(db_booking)
        db.commit()
        db.refresh(db_booking)
        return db_booking
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Booking already exists")

def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Booking).offset(skip).limit(limit).all(), db.query(models.Booking).count()

def get_booking(db: Session, booking_id: int):
    return db.query(models.Booking).filter(models.Booking.booking_id == booking_id).first()

def delete_booking(db: Session, booking_id: int):
    booking = db.query(models.Booking).filter(models.Booking.booking_id == booking_id).first()
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    db.delete(booking)
    db.commit()
    return {"message": "Booking deleted"}