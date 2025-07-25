# app/schemas/medicine.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from app.schemas.drug import DrugRead  # To show nested drugs

class MedicineBase(BaseModel):
    name: str
    manufacturer: Optional[str] = None
    batch_number: Optional[str] = None
    expiry_date: Optional[date] = None
    stock: Optional[int] = None
    price: Optional[float] = None
    category: Optional[str] = None
    status: Optional[int] = None

class MedicineCreate(MedicineBase):
    drugs: List[str]  # Accept list of drug IDs from the client

class MedicineRead(MedicineBase):
    id: int
    drugs: List[DrugRead] = []  # Return full drug objects

    class Config:
        orm_mode = True

class PaginatedMedicineRead(BaseModel):
    medicines: List[MedicineRead]
    total: int
    skip: int
    limit: int
    next_skip: Optional[int]
