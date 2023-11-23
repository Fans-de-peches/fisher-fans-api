from sqlalchemy.orm import Session
from .. import models, schemas
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def create_user(db: Session, user: schemas.UserCreate):
    try:
        hashed_password = "##" + user.password

        # Check if email already exists
        if db.query(models.User).filter(models.User.email == user.email).first():
            raise HTTPException(status_code=400, detail="Email already exists")

        db_user = models.User(**user.dict(exclude={"password"}), hashed_password=hashed_password)

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        raise HTTPException(status_code=400, detail="User already exists")

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    users = db.query(models.User).offset(skip).limit(limit).all()
    total = db.query(models.User).count()
    return users, total

def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    ...

def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}