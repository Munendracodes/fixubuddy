from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    manufacturer = Column(String(100))
    batch_number = Column(String(50))
    expiry_date = Column(Date)
    stock = Column(Integer)
    price = Column(Float)
    category = Column(String(50))
    status = Column(Integer, default = 1)

    # Many-to-Many: medicine <-> drugs (via compositions)
    drugs = relationship("Drug", secondary="compositions", back_populates="medicines")
