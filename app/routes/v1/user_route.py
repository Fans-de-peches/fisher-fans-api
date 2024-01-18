from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from ...services import user_service, security_service, boat_service, trip_service, booking_service, fishing_log_service
from ... import schemas, database
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users" , tags=["Users"])

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    user = user_service.create_user(db, user)
    return user

@router.put("/{id}", response_model=schemas.User)
def update_user(id: int, user: schemas.UserUpdate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    user = user_service.put_user(db, id, user)
    return user

@router.get("/", response_model=schemas.UserList)
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    users, total = user_service.get_users(db, skip, limit)
    return {"items": users, "total": total}

@router.get("/me/all", response_model=schemas.UserAllLists)
async def read_users_me_all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    boats, total_boats = boat_service.get_user_boats(db, current_user.user_id)
    trips, total_trips = trip_service.get_user_trips(db, current_user.user_id)
    bookings, total_bookings = booking_service.get_user_bookings(db, current_user.user_id)
    fishing_logs, total_fishing_logs = fishing_log_service.get_user_logs(db, current_user.user_id)
    return {"boats": {"items": boats, "total": total_boats}, "trips": {"items": trips, "total": total_trips}, "bookings": {"items": bookings, "total": total_bookings}, "fishing_logs": {"items": fishing_logs, "total": total_fishing_logs}}

@router.get("/me", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(security_service.get_current_user)):
    return current_user

@router.get("/{id}", response_model=schemas.User)
def get_user(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    user = user_service.get_user(db, id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    return user_service.delete_user(db, id)

# Routes about user items lists

@router.get("/{id}/boats", response_model=schemas.BoatList)
async def read_user_boats(id: int,db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    boats, total = boat_service.get_user_boats(db, id)
    return {"items": boats, "total": total} 

@router.get("/{id}/trips", response_model=schemas.TripList)
async def read_user_trips(id: int,db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    trips, total = trip_service.get_user_trips(db, id)
    return {"items": trips, "total": total}

@router.get("/{id}/bookings", response_model=schemas.BookingList)
async def read_user_bookings(id: int,db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    bookings, total = booking_service.get_user_bookings(db, id)
    return {"items": bookings, "total": total}

@router.get("/{id}/fishing_logs", response_model=schemas.FishingLogList)
async def read_user_fishing_logs(id: int,db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    fishing_logs, total = fishing_log_service.get_user_logs(db, id)
    return {"items": fishing_logs, "total": total}