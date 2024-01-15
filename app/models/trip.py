from sqlalchemy import Column, Integer, String, Date, Enum, Float, ForeignKey, TIMESTAMP, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.sqlite import JSON
from ..database import Base
import datetime

class Trip(Base):
    __tablename__ = "trip"

    trip_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    boat_id = Column(Integer, ForeignKey('boat.boat_id'))

    title = Column(String)
    infos = Column(String)
    trip_type = Column(Enum('daily', 'recurrent'))
    cost_type = Column(Enum('global', 'person'))
    date = Column(JSON)
    hours = Column(JSON)
    capacity = Column(Integer)
    cost = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)
    
    owner = relationship("User", back_populates="trips")
    bookings = relationship("Booking", back_populates="trip")
    boat = relationship("Boat", back_populates="trips")
