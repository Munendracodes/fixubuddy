# models/users.py
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)  # Optional, can ask after login
    mobile_number = Column(String, unique=True, nullable=False)

    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    area = Column(String, nullable=True)  # e.g., Rayachoti, Tirupati

    created_at = Column(DateTime(timezone=True), server_default=func.now())
