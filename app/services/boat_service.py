from sqlalchemy.orm import Session
from .. import models, schemas
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from datetime import datetime

def create_boat(db: Session, boat: schemas.BoatCreate):
    try:
        boat_data = boat.model_dump()
        user = db.query(models.User).filter(models.User.user_id == boat.user_id).first()
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        if user.boat_license_number is None:
            raise HTTPException(status_code=404, detail="User don\'t has boat license")
        
        if boat_data.get("birth_date"):
            boat_data["birth_date"] = datetime.strptime(boat_data["birth_date"], "%Y-%m-%d").date()
        db_boat = models.Boat(**boat_data)
        db.add(db_boat)
        db.commit()
        db.refresh(db_boat)
        return db_boat
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Boat already exists")

def get_boats(db: Session, skip: int = 0, limit: int = 100):
    boats = db.query(models.Boat).filter(models.Boat.user_id is not None).offset(skip).limit(limit).all()
    return boats, db.query(models.Boat).count()

def get_boats_by_zone(db: Session, zone: schemas.BoatZone, skip: int = 0, limit: int = 100):
    boatsAll = db.query(models.Boat).filter(
        models.Boat.longitude >= zone.x_min,
        models.Boat.longitude <= zone.x_max,
        models.Boat.latitude >= zone.y_min,
        models.Boat.latitude <= zone.y_max)
    boats = boatsAll.offset(skip).limit(limit).all()
    return boats, boatsAll.count()

def get_boat(db: Session, boat_id: int):
    return db.query(models.Boat).filter(models.Boat.boat_id == boat_id).first()

def get_user_boats(db: Session, user_id: int):
    boats = db.query(models.Boat).filter(models.Boat.user_id == user_id).all()
    return boats, len(boats)

def update_boat(db: Session, boat_id: int, boat: schemas.BoatCreate):
    db_boat = db.query(models.Boat).filter(models.Boat.boat_id == boat_id).first()
    if db_boat is None:
        raise HTTPException(status_code=404, detail="Boat not found")
    else:
        boat_data = boat.model_dump()
        if boat_data.get("birth_date"):
            boat_data["birth_date"] = datetime.strptime(boat_data["birth_date"], "%Y-%m-%d").date()
        for var, value in vars(boat).items():
            if value is not None:
                setattr(db_boat, var, value)
        db.commit()
        db.refresh(db_boat)
        return db_boat

def delete_boat(db: Session, boat_id: int):
    boat = db.query(models.Boat).filter(models.Boat.boat_id == boat_id).first()
    if boat is None:
        raise HTTPException(status_code=404, detail="Boat not found")
    db.delete(boat)
    db.commit()
    return {"message": "Boat deleted"}