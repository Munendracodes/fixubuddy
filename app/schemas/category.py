# app/schemas/category.py
from pydantic import BaseModel

class CategoryOut(BaseModel):
    id: int
    name: str
    category: str
    icon_url: str | None

    class Config:
        orm_mode = True
