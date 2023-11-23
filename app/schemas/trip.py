from pydantic import BaseModel
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
    pass

class TripUpdate(TripBase):
    pass

class Trip(TripBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class TripList(BaseModel):
    items: List[Trip]
    total: int
