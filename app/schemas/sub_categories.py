from pydantic import BaseModel
from typing import Optional, List
from app.schemas.technician import TechnicianResponseinSubCategories

class SubCategoryBase(BaseModel):
    name: str
    image_url: Optional[str] = None

class SubCategoryCreate(SubCategoryBase):
    pass

class SubCategoryResponse(BaseModel):
    id: int
    name: str
    image_url: Optional[str]
    category_id: int

    class Config:
        orm_mode = True
        
class SubCategoryTechnicianResponse(BaseModel):
    id: int
    name: str
    technicians: List[TechnicianResponseinSubCategories]
