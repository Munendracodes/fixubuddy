from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Drug(Base):
    __tablename__ = "drugs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

    # Many-to-Many: drug <-> medicines (via compositions)
    medicines = relationship("Medicine", secondary="compositions", back_populates="drugs")
