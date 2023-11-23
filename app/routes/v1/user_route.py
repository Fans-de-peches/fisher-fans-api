# routes/user_routes.py
from fastapi import APIRouter, Depends
from ...services import user_service
from ... import schemas, database
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users")

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return user_service.create_user(db, user)

# Et ainsi de suite pour les autres routes
