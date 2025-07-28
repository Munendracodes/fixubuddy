from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.sub_categories import SubCategory
from app.models.categories import Category
from app.models.technician_subcategories import TechnicianSubCategory
from app.schemas.sub_categories import SubCategoryCreate, SubCategoryResponse
from app.database import get_db

router = APIRouter(prefix="/sub_categories", tags=["Sub Categories"])

@router.post("/", response_model=SubCategoryResponse)
def create_sub_category(sub_cat: SubCategoryCreate, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.name == sub_cat.category_name).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    new_sub = SubCategory(
        name=sub_cat.name,
        image_url=sub_cat.image_url,
        category_id=category.id
    )
    db.add(new_sub)
    db.commit()
    db.refresh(new_sub)
    return SubCategoryResponse(
        id=new_sub.id,
        name=new_sub.name,
        image_url=new_sub.image_url,
        category_id=new_sub.category_id,
        technician_ids=[]
    )

@router.get("/", response_model=list[SubCategoryResponse])
def get_all_sub_categories(db: Session = Depends(get_db)):
    sub_categories = db.query(SubCategory).all()
    result = []
    for sub in sub_categories:
        tech_ids = [link.technician_id for link in sub.technicians]
        result.append(SubCategoryResponse(
            id=sub.id,
            name=sub.name,
            image_url=sub.image_url,
            category_id=sub.category_id,
            technician_ids=tech_ids
        ))
    return result

@router.get("/{id}", response_model=SubCategoryResponse)
def get_sub_category_by_id(id: int, db: Session = Depends(get_db)):
    sub = db.query(SubCategory).filter(SubCategory.id == id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="SubCategory not found")
    tech_ids = [link.technician_id for link in sub.technicians]
    return SubCategoryResponse(
        id=sub.id,
        name=sub.name,
        image_url=sub.image_url,
        category_id=sub.category_id,
        technician_ids=tech_ids
    )
