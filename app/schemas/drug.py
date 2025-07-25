# app/schemas/drug.py
from pydantic import BaseModel
from typing import List, Optional

class DrugBase(BaseModel):
    name: str

class DrugCreate(DrugBase):
    pass

class DrugRead(DrugBase):
    id: int

    class Config:
        orm_mode = True
        
class PaginatedDrugRead(BaseModel):
    drugs: List[DrugRead]
    total: int
    skip: int
    limit: int
    next_skip: Optional[int]
    
class DrugListCreate(BaseModel):
    drugs: List[DrugCreate]
    
    
