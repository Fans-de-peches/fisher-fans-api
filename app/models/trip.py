from sqlalchemy import Column, Integer, String, Date, Enum, Float, ForeignKey, TIMESTAMP, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.sqlite import JSON
from .database import Base
import datetime

class Trip(Base):
    __tablename__ = "trip"

    trip_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    infos = Column(String)
    trip_type = Column(Enum('daily', 'recurrent'))
    cost_type = Column(Enum('global', 'person'))
    date = Column(JSON)
    # Assuming hours is an JSON)
    hours = Column(JSON)
    capacity = Column(Integer)
    cost = Column(Float)
    owner_id = Column(Integer, ForeignKey('user.user_id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    owner = relationship("User", back_populates="trips")
