from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Technician(Base):
    __tablename__ = "technicians"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)             # ✅ Added length
    mobile = Column(String(15), nullable=False)            # ✅ Mobile numbers are usually 10–15 digits
    work = Column(String(100), nullable=True)              # ✅ Optional, added length
    description = Column(String(500), nullable=True)       # ✅ Optional description
    rating = Column(Float, nullable=True)
    image_url = Column(String(255), nullable=True)         # ✅ For URL storage

    sub_category_links = relationship("TechnicianSubCategory", back_populates="technician")
