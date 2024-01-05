from fastapi import APIRouter, Depends, HTTPException
from ...services import user_service
from ... import schemas, database
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users" , tags=["Users"])

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    user = user_service.create_user(db, user)
    return user

# TODO finir la route update_user
@router.put("/{id}", response_model=schemas.User)
def update_user(id: int, user: schemas.UserUpdate, db: Session = Depends(database.get_db)):
    update_user = user_service.update_user(db, id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.get("/", response_model=schemas.UserList)
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    users, total = user_service.get_users(db, skip, limit)
    return {"items": users, "total": total}

@router.get("/{id}", response_model=schemas.User)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = user_service.get_user(db, id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(database.get_db)):
    return user_service.delete_user(db, id)