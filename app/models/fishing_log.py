from sqlalchemy import Column, Integer, String, Date, Enum, Float, ForeignKey, TIMESTAMP, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.sqlite import JSON
from .database import Base
import datetime

class FishingLog(Base):
    __tablename__ = "fishing_log"

    log_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('user.user_id'))
    fish_name = Column(String)
    image = Column(String)
    comment = Column(String)
    height = Column(Float)
    weight = Column(Float)
    fishing_place = Column(String)
    fishing_date = Column(Date)
    leaved = Column(Boolean)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)

    owner = relationship("User", back_populates="logs")
