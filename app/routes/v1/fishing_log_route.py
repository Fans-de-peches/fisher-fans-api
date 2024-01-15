from fastapi import APIRouter, Depends, HTTPException
from ...services import fishing_log_service, security_service
from ... import schemas, database
from sqlalchemy.orm import Session
from pydantic import ValidationError

router = APIRouter(prefix="/logs" , tags=["Fishing Logs"])

@router.post("/", response_model=schemas.FishingLog)
def create_log(log: schemas.FishingLogCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    try:
        return fishing_log_service.create_log(db, log)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

@router.put("/{id}", response_model=schemas.FishingLog)
def update_log(id: int, log: schemas.FishingLogUpdate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    log = fishing_log_service.update_log(db, id, log)
    return log

@router.get("/", response_model=schemas.FishingLogList)
def get_logs(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    logs, total = fishing_log_service.get_logs(db, skip, limit)
    return {"items": logs, "total": total}

@router.get("/{id}", response_model=schemas.FishingLog)
def get_log(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    log = fishing_log_service.get_log(db, id)
    if log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return log

@router.delete("/{id}")
def delete_log(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(security_service.get_current_user)):
    return fishing_log_service.delete_log(db, id)