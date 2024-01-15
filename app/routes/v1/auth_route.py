from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ... import schemas, models
from ...services import security_service
from ...schemas.token import Token, UserCredentials
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta

router = APIRouter(tags=["Authentication"])

ACCESS_TOKEN_EXPIRE_MINUTES = 30

@router.post("/auth", response_model=Token)
async def login_for_access_token(
    form_data: UserCredentials = Body(...),
    db: Session = Depends(security_service.get_db)
):
    user = db.query(models.User).filter(models.User.email == form_data.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not security_service.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security_service.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/auth/refresh", response_model=Token)
async def refresh_access_token(
    current_user: models.User = Depends(security_service.get_current_user)
):
    access_token = security_service.create_access_token(
        data={"sub": current_user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
