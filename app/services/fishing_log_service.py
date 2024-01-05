from sqlalchemy.orm import Session
from .. import models, schemas
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from datetime import datetime

def create_log(db: Session, log: schemas.FishingLogCreate):
    try:
        log_data = log.model_dump()
        user = db.query(models.User).filter(models.User.user_id == log.owner_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if log_data.get("fishing_date"):
            log_data["fishing_date"] = datetime.strptime(log_data["fishing_date"], "%Y-%m-%d").date()
        db_log = models.FishingLog(**log_data)
        db.add(db_log)
        db.commit()
        db.refresh(db_log)
        return db_log
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Log already exists")

def get_logs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FishingLog).offset(skip).limit(limit).all(), db.query(models.FishingLog).count()

def get_log(db: Session, log_id: int):
    return db.query(models.FishingLog).filter(models.FishingLog.log_id == log_id).first()

def delete_log(db: Session, log_id: int):
    log = db.query(models.FishingLog).filter(models.FishingLog.log_id == log_id).first()
    if log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    db.delete(log)
    db.commit()
    return {"message": "Log deleted"}