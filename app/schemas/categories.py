from pydantic import BaseModel
from typing import List, Optional
from app.schemas.sub_categories import SubCategoryResponse

class CategoryBase(BaseModel):
    name: str
    image_url: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class CategorySubCategoryResponse(CategoryResponse):
    sub_categories: List[SubCategoryResponse]
