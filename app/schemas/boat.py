from pydantic import BaseModel, validator
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
    description: Optional[str]
    manufacturer: Optional[str]
    birth_date: Optional[date]
    image: Optional[str]
    license_type: LicenseTypeEnum
    boat_type: BoatTypeEnum
    equipment: List[str]
    deposit_amount: float
    max_capacity: int
    sleeping_capacity: int
    home_port: str
    home_city: str
    coordinate: str
    motor_type: Optional[MotorTypeEnum]
    motor_power: Optional[int]
    boat_status: BoatStatusEnum

class BoatCreate(BoatBase):
    birth_date: Optional[str]

    @validator('birth_date', pre=True)
    def validate_birth_date(cls, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            raise ValueError("Invalid birth_date format")

class BoatUpdate(BoatBase):
    pass

class Boat(BoatBase):
    boat_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

class BoatList(BaseModel):
    items: List[Boat]
    total: int