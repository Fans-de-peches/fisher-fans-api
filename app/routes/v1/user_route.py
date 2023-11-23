from fastapi import APIRouter, Depends
from ...services import user_service
from ... import schemas, database
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users" , tags=["Users"])

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return user_service.create_user(db, user)

@router.get("/", response_model=schemas.UserList)
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    users, total = user_service.get_users(db, skip, limit)
    return {"items": users, "total": total}

@router.get("/{id}", response_model=schemas.User)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user_service.get_user(db, id)

@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(database.get_db)):
    return user_service.delete_user(db, id)