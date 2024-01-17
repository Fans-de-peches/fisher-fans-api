from sqlalchemy.orm import Session
from .. import models, schemas
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from datetime import datetime

def create_trip(db: Session, trip: schemas.TripCreate):
    user = db.query(models.User).filter(models.User.user_id == trip.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    has_boat = db.query(models.Boat).filter(models.Boat.user_id == user.user_id).first() 
    
    if not has_boat:
        raise HTTPException(status_code=404, detail="User don\'t has boat found")
    db_trip = models.Trip(**trip.model_dump())
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip

def get_trips(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Trip).offset(skip).limit(limit).all(), db.query(models.Trip).count()

def get_user_trips(db: Session, user_id: int):
    trips = db.query(models.Trip).filter(models.Trip.user_id == user_id).all()
    return trips, len(trips)

def get_trip(db: Session, trip_id: int):
    return db.query(models.Trip).filter(models.Trip.trip_id == trip_id).first()

def update_trip(db: Session, trip_id: int, trip: schemas.TripUpdate):
    db_trip = db.query(models.Trip).filter(models.Trip.trip_id == trip_id).first()
    if db_trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    for var, value in vars(trip).items():
        if value is not None:
            setattr(db_trip, var, value)
    db.commit()
    db.refresh(db_trip)
    return db_trip

def delete_trip(db: Session, trip_id: int):
    trip = db.query(models.Trip).filter(models.Trip.trip_id == trip_id).first()
    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    db.delete(trip)
    db.commit()
    return {"message": "Trip deleted"}