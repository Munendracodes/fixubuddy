from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Technician(Base):
    __tablename__ = "technicians"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    mobile = Column(String, nullable=False)
    work = Column(String)
    description = Column(String)
    rating = Column(Float)
    image_url = Column(String)

    sub_category_links = relationship("TechnicianSubCategory", back_populates="technician")
