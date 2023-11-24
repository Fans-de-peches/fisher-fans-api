from fastapi import APIRouter, Depends, HTTPException
from ...services import boat_service
from ... import schemas, database
from sqlalchemy.orm import Session
from pydantic import ValidationError

router = APIRouter(prefix="/boats" , tags=["Boats"])

@router.post("/", response_model=schemas.Boat)
def create_boat(boat: schemas.BoatCreate, db: Session = Depends(database.get_db)):
    try:
        return boat_service.create_boat(db, boat)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

# TODO finir la route update_boat
@router.put("/{id}", response_model=schemas.Boat)
def update_boat(id: int, boat: schemas.BoatCreate, db: Session = Depends(database.get_db)):
    try:
        return boat_service.update_boat(db, id, boat)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

@router.get("/", response_model=schemas.BoatList)
def get_boats(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    boats, total = boat_service.get_boats(db, skip, limit)
    return {"items": boats, "total": total}

@router.get("/{id}", response_model=schemas.Boat)
def get_boat(id: int, db: Session = Depends(database.get_db)):
    boat = boat_service.get_boat(db, id)
    if boat is None:
        raise HTTPException(status_code=404, detail="Boat not found")
    return boat

@router.delete("/{id}")
def delete_boat(id: int, db: Session = Depends(database.get_db)):
    return boat_service.delete_boat(db, id)