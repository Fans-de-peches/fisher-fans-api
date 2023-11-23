from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime
from enum import Enum

class StatusEnum(str, Enum):
    particulier = "particulier"
    professionnel = "professionnel"

class ActivityEnum(str, Enum):
    location = "location"
    guide = "guide"

class UserBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: Optional[date]
    email: str
    mobile: str
    address: str
    zip_code: int
    city: str
    languages: List[str]
    avatar_url: Optional[str]
    boat_license_number: Optional[int]
    insurance_number: Optional[str]
    status: StatusEnum
    company_name: Optional[str]
    activity_type: Optional[ActivityEnum]
    siret_number: Optional[str]
    commerce_registry_number: Optional[str]

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str]

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UserList(BaseModel):
    items: List[User]
    total: int
