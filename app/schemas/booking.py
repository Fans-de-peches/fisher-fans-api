from pydantic import field_validator, ConfigDict, BaseModel
from typing import List, Optional
from datetime import date, datetime
from enum import Enum

# Booking Schemas
class BookingBase(BaseModel):
    user_id: int
    trip_id: int
    date: date
    reserved_users: int
    total_cost: float

class BookingCreate(BookingBase):
    date: Optional[str] = None
    
    @field_validator('date', mode="before")
    @classmethod
    def validate_date(cls, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            raise ValueError("Invalid date format")

class BookingUpdate(BookingBase):
    pass

class Booking(BookingBase):
    booking_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)

class BookingList(BaseModel):
    items: List[Booking]
    total: int