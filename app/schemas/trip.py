from pydantic import field_validator, ConfigDict, BaseModel
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
    user_id: int
    title: str
    infos: Optional[str] = None
    trip_type: TripTypeEnum
    cost_type: CostTypeEnum
    date: List[str]
    hours: List[str]
    capacity: int
    cost: float

class TripCreate(TripBase):
    date: Optional[List[str]] = None  # Accepte une chaîne JSON représentant une liste de dates
    hours: Optional[List[str]] = None  # Accepte une chaîne JSON représentant une liste d'heures

    @field_validator('date')
    @classmethod
    def validate_date(cls, v):
        if v:
            return v
        else:
            return []
    
    @field_validator('hours')
    @classmethod
    def validate_hours(cls, v):
        if v:
            return v
        else:
            return []

class TripUpdate(TripBase):
    date: Optional[List[str]] = None  # Accepte une chaîne JSON représentant une liste de dates
    hours: Optional[List[str]] = None  # Accepte une chaîne JSON représentant une liste d'heures
    
    @field_validator('date')
    @classmethod
    def validate_date(cls, v):
        if v:
            return v
        else:
            return []
    
    @field_validator('hours')
    @classmethod
    def validate_hours(cls, v):
        if v:
            return v
        else:
            return []

class Trip(TripBase):
    trip_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)

class TripList(BaseModel):
    items: List[Trip]
    total: int
