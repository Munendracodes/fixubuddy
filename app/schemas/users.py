# schemas/users.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# 🧱 Base schema shared by create/response
class UserBase(BaseModel):
    mobile_number: str = Field(..., example="9876543210", min_length=10, max_length=15)
    name: Optional[str] = Field(None, example="Munendra")
    latitude: Optional[float] = Field(None, example=14.056)
    longitude: Optional[float] = Field(None, example=78.789)
    area: Optional[str] = Field(None, example="Rayachoti")


# 📥 For user creation
class UserCreate(UserBase):
    pass


# 📝 For user update
class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, example="Munendra")
    latitude: Optional[float] = Field(None, example=14.056)
    longitude: Optional[float] = Field(None, example=78.789)
    area: Optional[str] = Field(None, example="Rayachoti")


# 📤 For user response (DB output)
class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
