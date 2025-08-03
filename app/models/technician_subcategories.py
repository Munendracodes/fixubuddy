from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class TechnicianSubCategory(Base):
    __tablename__ = "technician_subcategories"

    technician_id = Column(Integer, ForeignKey("technicians.id"), primary_key=True)
    sub_category_id = Column(Integer, ForeignKey("sub_categories.id"), primary_key=True)

    technician = relationship("Technician", back_populates="sub_category_links")
    sub_category = relationship("SubCategory", back_populates="technicians")
