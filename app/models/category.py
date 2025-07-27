# app/models/category.py
from sqlalchemy import Column, Integer, String
from app.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    icon_url = Column(String, nullable=True)
