from sqlalchemy import Column, Integer, String, Date, Enum, Float, ForeignKey, TIMESTAMP, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.sqlite import JSON
from .database import Base
import datetime

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    email = Column(String, unique=True, index=True)
    mobile = Column(String)
    hashed_password = Column(String, index=True)
    address = Column(String)
    zip_code = Column(Integer)
    city = Column(String)
    languages = Column(JSON)
    avatar_url = Column(String)
    boat_license_number = Column(Integer)
    insurance_number = Column(String)
    status = Column(Enum('particulier', 'professionnel'))
    company_name = Column(String)
    activity_type = Column(Enum('location', 'guide'))
    siret_number = Column(String)
    commerce_registry_number = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    boats = relationship("Boat", back_populates="owner")
    logs = relationship("FishingLog", back_populates="owner")
    trips = relationship("Trip", back_populates="owner")
    bookings = relationship("Booking", back_populates="owner")
