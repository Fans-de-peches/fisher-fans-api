from pydantic import field_validator, ConfigDict, BaseModel
from typing import List, Optional
from datetime import date, datetime
from enum import Enum

class LicenseTypeEnum(str, Enum):
    cotier = "cotier"
    fluvial = "fluvial"

class BoatTypeEnum(str, Enum):
    open = "open"
    cabine = "cabine"
    catamaran = "catamaran"
    voilier = "voilier"
    jetski = "jetski"
    canoe = "canoe"

class BoatStatusEnum(str, Enum):
    active = "active"
    disable = "disable"

class MotorTypeEnum(str, Enum):
    diesel = "diesel"
    essence = "essence"

# Boat Schemas
class BoatBase(BaseModel):
    user_id: int
    name: str
    description: Optional[str] = None
    manufacturer: Optional[str] = None
    birth_date: Optional[date] = None
    image: Optional[str] = None
    license_type: LicenseTypeEnum
    boat_type: BoatTypeEnum
    equipment: List[str]
    deposit_amount: float
    max_capacity: int
    sleeping_capacity: int
    home_port: str
    home_city: str
    longitude: float
    latitude: float
    motor_type: Optional[MotorTypeEnum] = None
    motor_power: Optional[int] = None
    boat_status: BoatStatusEnum
    model_config = ConfigDict(from_attributes=True)

class BoatCreate(BoatBase):
    birth_date: Optional[str] = None
    
    @field_validator('birth_date', mode="before")
    @classmethod
    def validate_birth_date(cls, value):
        try:
            if value:
                datetime.strptime(value, "%Y-%m-%d")
                return value
            else:
                return None
        except ValueError:
            raise ValueError("Invalid birth_date format")

class BoatUpdate(BoatCreate):
    pass

class Boat(BoatBase):
    boat_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

class BoatZone (BaseModel):
    x_min: float
    x_max: float
    y_min: float
    y_max: float

class BoatList(BaseModel):
    items: List[Boat]
    total: int