# app/routes/category.py
import os
import uuid
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryOut
from app.database import get_db
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

UPLOAD_DIR = "app/static/icons"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/", response_model=CategoryOut)
def create_category(
    name: str = Form(...),
    category: str = Form(...),
    icon: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Validate file type
    if not icon.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed")

    # Generate unique filename
    ext = icon.filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4()}.{ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    # Save image
    with open(file_path, "wb") as f:
        f.write(icon.file.read())

    # Create DB entry
    icon_url = f"/static/icons/{unique_filename}"  # exposed path
    new_category = Category(name=name, category=category, icon_url=icon_url)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@router.get("/", response_model=list[CategoryOut])
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()
