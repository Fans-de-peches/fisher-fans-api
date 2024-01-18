from pydantic import field_validator, ConfigDict, BaseModel
from typing import List, Optional
from datetime import date, datetime
from enum import Enum

# FishingLog Schemas
class FishingLogBase(BaseModel):
    user_id: int | None
    fish_name: str
    image: Optional[str] = None
    comment: Optional[str] = None
    height: float
    weight: float
    fishing_place: str
    fishing_date: date
    leaved: bool

class FishingLogCreate(FishingLogBase):
    fishing_date: Optional[str] = None

    @field_validator('fishing_date', mode="before")
    @classmethod
    def validate_fishing_date(cls, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            raise ValueError("Invalid fishing_date format")

class FishingLogUpdate(FishingLogBase):
    pass

class FishingLog(FishingLogBase):
    log_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)

class FishingLogList(BaseModel):    
    items: List[FishingLog]
    total: int
