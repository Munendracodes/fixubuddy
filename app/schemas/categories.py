from pydantic import BaseModel
from typing import List, Optional

class CategoryBase(BaseModel):
    name: str
    image_url: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    sub_category_ids: List[int] = []

    class Config:
        orm_mode = True
