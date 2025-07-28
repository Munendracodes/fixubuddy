from pydantic import BaseModel
from typing import List, Optional

class TechnicianBase(BaseModel):
    name: str
    mobile: str
    work: str
    description: Optional[str]
    rating: Optional[float]
    image_url: Optional[str]

class TechnicianCreate(TechnicianBase):
    sub_category_ids: List[int]

class SubCategoryInfo(BaseModel):
    id: int
    name: str
    category_id: int
    image_url: Optional[str]

    class Config:
        orm_mode = True

class CategoryInfo(BaseModel):
    id: int
    name: str
    image_url: Optional[str]

    class Config:
        orm_mode = True

class TechnicianResponse(TechnicianBase):
    id: int
    sub_category_info: List[SubCategoryInfo]
    category_info: List[CategoryInfo]

    class Config:
        orm_mode = True
