from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.categories import Category
from app.models.sub_categories import SubCategory
from app.schemas.categories import CategoryCreate, CategoryResponse, CategorySubCategoryResponse
from app.database import get_db
from typing import List

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=List[CategoryResponse])
def create_categories(categories: List[CategoryCreate], db: Session = Depends(get_db)):
    db_inserted_data = []

    for category in categories:
        exist_data = db.query(Category).filter(Category.name == category.name).first()
        if not exist_data:
            db_category = Category(**category.dict())
            db.add(db_category)
            db_inserted_data.append(db_category)
        else:
            db_inserted_data.append(exist_data)

    db.commit()  # ✅ Commit once, better performance
    for category in db_inserted_data:
        db.refresh(category)  # ✅ Refresh to get updated values like id

    return db_inserted_data


@router.get("/", response_model=list[CategoryResponse])
def get_all_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    result = []
    for cat in categories:
        sub_ids = [sub.id for sub in cat.sub_categories]
        result.append(CategoryResponse(
            id=cat.id,
            name=cat.name,
            image_url=cat.image_url,
            sub_category_ids=sub_ids
        ))
    return result

@router.get("/{id}", response_model=CategorySubCategoryResponse)
def get_category_by_id(id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category
