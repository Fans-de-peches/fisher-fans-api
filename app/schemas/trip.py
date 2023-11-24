from pydantic import BaseModel, validator
from typing import List, Optional
from datetime import date, datetime
from enum import Enum

class TripTypeEnum(str, Enum):
    peche = "daily"
    promenade = "recurrent"

class CostTypeEnum(str, Enum):
    peche = "global"
    promenade = "person"

# Trip Schemas
class TripBase(BaseModel):
    title: str
    infos: Optional[str]
    trip_type: TripTypeEnum
    cost_type: CostTypeEnum
    date: List[str]
    hours: List[str]
    capacity: int
    cost: float
    owner_id: int

class TripCreate(TripBase):
    date: Optional[List[str]]  # Accepte une chaîne JSON représentant une liste de dates
    hours: Optional[List[str]]  # Accepte une chaîne JSON représentant une liste d'heures

    @validator('date')
    def validate_date(cls, v):
        if v:
            return v
        else:
            return []
    
    @validator('hours')
    def validate_hours(cls, v):
        if v:
            return v
        else:
            return []

class TripUpdate(TripBase):
    pass

class Trip(TripBase):
    trip_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

class TripList(BaseModel):
    items: List[Trip]
    total: int
