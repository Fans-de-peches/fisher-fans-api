from sqlalchemy.orm import Session
from .. import models, schemas
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from datetime import datetime

def create_boat(db: Session, boat: schemas.BoatCreate):
    try:
        boat_data = boat.model_dump()
        user = db.query(models.User).filter(models.User.user_id == boat.owner_id).first()
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
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
    return db.query(models.Boat).offset(skip).limit(limit).all(), db.query(models.Boat).count()

def get_boat(db: Session, boat_id: int):
    return db.query(models.Boat).filter(models.Boat.boat_id == boat_id).first()

def delete_boat(db: Session, boat_id: int):
    boat = db.query(models.Boat).filter(models.Boat.boat_id == boat_id).first()
    if boat is None:
        raise HTTPException(status_code=404, detail="Boat not found")
    db.delete(boat)
    db.commit()
    return {"message": "Boat deleted"}