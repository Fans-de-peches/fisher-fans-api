from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime
from enum import Enum

# FishingLog Schemas
class FishingLogBase(BaseModel):
    owner_id: int
    fish_name: str
    image: Optional[str]
    comment: Optional[str]
    height: float
    weight: float
    fishing_place: str
    fishing_date: str
    leaved: bool

class FishingLogCreate(FishingLogBase):
    pass

class FishingLogUpdate(FishingLogBase):
    pass

class FishingLog(FishingLogBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class FishingLogList(BaseModel):    
    items: List[FishingLog]
    total: int
