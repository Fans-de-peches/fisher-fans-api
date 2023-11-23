from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime
from enum import Enum

# Booking Schemas
class BookingBase(BaseModel):
    trip_id: int
    date_: str
    reserved_users: int
    total_cost: float
    owner_id: int

class BookingCreate(BookingBase):
    pass

class BookingUpdate(BookingBase):
    pass

class Booking(BookingBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class BookingList(BaseModel):
    items: List[Booking]
    total: int