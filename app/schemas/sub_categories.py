from pydantic import BaseModel
from typing import Optional, List

class SubCategoryBase(BaseModel):
    name: str
    image_url: Optional[str] = None
    category_name: str  # Used during creation

class SubCategoryCreate(SubCategoryBase):
    pass

class SubCategoryResponse(BaseModel):
    id: int
    name: str
    image_url: Optional[str]
    category_id: int
    technician_ids: List[int] = []

    class Config:
        orm_mode = True
