from sqlalchemy import Column, Integer, String, Date, Enum, Float, ForeignKey, TIMESTAMP, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.sqlite import JSON
from ..database import Base
import datetime

class Booking(Base):
    __tablename__ = "booking"

    booking_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    trip_id = Column(Integer, ForeignKey('trip.trip_id'))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    
    date_ = Column(Date)
    reserved_users = Column(Integer)
    total_cost = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)

    owner = relationship("User", back_populates="bookings")
    trip = relationship("Trip", back_populates="bookings")