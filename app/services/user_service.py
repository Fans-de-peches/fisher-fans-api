from sqlalchemy.orm import Session
from .. import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    # Logique pour créer un utilisateur
    ...

def get_user(db: Session, user_id: int):
    # Logique pour lire un utilisateur
    ...

def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    # Logique pour mettre à jour un utilisateur
    ...

def delete_user(db: Session, user_id: int):
    # Logique pour supprimer un utilisateur
    ...
