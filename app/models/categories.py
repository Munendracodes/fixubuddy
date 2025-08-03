from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)      # ✅ Added length
    image_url = Column(String(255), nullable=True)               # ✅ Added length

    sub_categories = relationship("SubCategory", back_populates="category")
