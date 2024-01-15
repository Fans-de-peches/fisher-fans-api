from pydantic import ConfigDict, BaseModel
from typing import List, Optional
from datetime import date, datetime
from enum import Enum
from .boat import BoatList
from .trip import TripList
from .booking import BookingList
from .fishing_log import FishingLogList

class StatusEnum(str, Enum):
    particulier = "particulier"
    professionnel = "professionnel"

class ActivityEnum(str, Enum):
    location = "location"
    guide = "guide"

class UserBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: Optional[date] = None
    email: str
    mobile: str
    address: str
    zip_code: int
    city: str
    languages: List[str]
    avatar_url: Optional[str] = None
    boat_license_number: Optional[int] = None
    insurance_number: Optional[str] = None
    status: StatusEnum
    company_name: Optional[str] = None
    activity_type: Optional[ActivityEnum] = None
    siret_number: Optional[str] = None
    commerce_registry_number: Optional[str] = None

class UserCreate(UserBase):
    password: str
    
class UserUpdate(UserBase):
    password: Optional[str] = None

class User(UserBase):
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

class UserList(BaseModel):
    items: List[User]
    total: int

class UserAllLists(BaseModel):
    boats: BoatList
    trips: TripList
    bookings: BookingList
    fishing_logs: FishingLogList