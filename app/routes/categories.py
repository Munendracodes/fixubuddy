from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.categories import Category
from app.models.sub_categories import SubCategory
from app.schemas.categories import CategoryCreate, CategoryResponse
from app.database import get_db

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = Category(name=category.name, image_url=category.image_url)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return CategoryResponse(
        id=db_category.id,
        name=db_category.name,
        image_url=db_category.image_url,
        sub_category_ids=[]
    )

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

@router.get("/{id}", response_model=CategoryResponse)
def get_category_by_id(id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    sub_ids = [sub.id for sub in category.sub_categories]
    return CategoryResponse(
        id=category.id,
        name=category.name,
        image_url=category.image_url,
        sub_category_ids=sub_ids
    )
