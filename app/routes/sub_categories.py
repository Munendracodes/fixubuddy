from fastapi import APIRouter, Depends, HTTPException, Query, Body
from sqlalchemy.orm import Session
from app.models.sub_categories import SubCategory
from app.models.categories import Category
from app.schemas.sub_categories import SubCategoryCreate, SubCategoryResponse, SubCategoryTechnicianResponse
from app.database import get_db
from typing import List

router = APIRouter(prefix="/sub_categories", tags=["Sub Categories"])


@router.post("/", response_model=List[SubCategoryResponse])
def create_sub_categories(
    category_name: str = Query(..., description="Name of the category"),
    sub_cat_list: List[SubCategoryCreate] = Body(...),
    db: Session = Depends(get_db)
):
    category = db.query(Category).filter(Category.name == category_name).first()
    if not category:
        raise HTTPException(status_code=404, detail=f"Category '{category_name}' not found")

    created_subcategories = []
    for sub_cat in sub_cat_list:
        db_sub = SubCategory(**sub_cat.dict(), category_id=category.id)
        db.add(db_sub)
        db.commit()
        db.refresh(db_sub)
        created_subcategories.append(db_sub)

    return created_subcategories


@router.get("/{id}", response_model=SubCategoryTechnicianResponse)
def get_sub_category_by_id(id: int, db: Session = Depends(get_db)):
    sub = db.query(SubCategory).filter(SubCategory.id == id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="SubCategory not found")

    # Manually collect technician info from TechnicianSubCategory
    technicians = []
    for tech_sub in sub.technicians:
        tech = tech_sub.technician  # assuming there's a `technician` relationship in TechnicianSubCategory
        technicians.append({
            "id": tech.id,
            "name": tech.name,
            "mobile": tech.mobile,
            "work": tech.work,
            "description": tech.description,
            "rating": tech.rating,
            "image_url": tech.image_url,
        })

    return {
        "id": sub.id,
        "name": sub.name,
        "technicians": technicians
    }

