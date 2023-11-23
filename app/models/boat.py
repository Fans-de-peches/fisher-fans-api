from sqlalchemy import Column, Integer, String, Date, Enum, Float, ForeignKey, TIMESTAMP, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.sqlite import JSON
from ..database import Base
import datetime

class Boat(Base):
    __tablename__ = "boat"

    boat_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    name = Column(String)
    description = Column(String)
    manufacturer = Column(String)
    birth_date = Column(Date)
    image = Column(String)
    license_type = Column(Enum('cotier', 'fluvial'))
    boat_type = Column(Enum('open', 'cabine', 'catamaran', 'voilier', 'jetski', 'canoe'))
    equipment = Column(JSON)
    deposit_amount = Column(Float)
    max_capacity = Column(Integer)
    sleeping_capacity = Column(Integer)
    home_port = Column(String)
    home_city = Column(String)
    coordinate = Column(String)
    motor_type = Column(Enum('diesel', 'essence'))
    motor_power = Column(Integer)
    boat_status = Column(Enum('active', 'disable'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)
    owner = relationship("User", back_populates="boats")
