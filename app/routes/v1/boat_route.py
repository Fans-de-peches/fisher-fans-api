from fastapi import APIRouter, Depends, HTTPException
from ...services import boat_service, security_service
from ... import schemas, database
from sqlalchemy.orm import Session
from pydantic import ValidationError

router = APIRouter(prefix="/boats" , tags=["Boats"])

@router.post("/", response_model=schemas.Boat)
def create_boat(boat: schemas.BoatCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    try:
        return boat_service.create_boat(db, boat)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

@router.put("/{id}", response_model=schemas.Boat)
def update_boat(id: int, boat: schemas.BoatCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    boat = boat_service.update_boat(db, id, boat)
    return boat

@router.get("/", response_model=schemas.BoatList)
def get_boats(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    boats, total = boat_service.get_boats(db, skip, limit)
    return {"items": boats, "total": total}

@router.get("/search_zone", response_model=schemas.BoatList)
def get_boats_by_zone(x_min:float = 0, x_max:float = 0, y_min:float = 0, y_max:float = 0, 
        skip: int = 0, limit: int = 100,
        db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    zone = schemas.BoatZone(x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max)
    boats, total = boat_service.get_boats_by_zone(db, zone, skip, limit)
    return {"items": boats, "total": total}

@router.get("/{id}", response_model=schemas.Boat)
def get_boat(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    boat = boat_service.get_boat(db, id)
    if boat is None:
        raise HTTPException(status_code=404, detail="Boat not found")
    return boat

@router.delete("/{id}")
def delete_boat(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    return boat_service.delete_boat(db, id)