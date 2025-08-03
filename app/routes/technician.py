from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.technician import Technician
from app.models.sub_categories import SubCategory
from app.models.categories import Category
from app.models.technician_subcategories import TechnicianSubCategory
from app.schemas.technician import TechnicianCreate, TechnicianResponse, SubCategoryInfo, CategoryInfo
from app.database import get_db

router = APIRouter(prefix="/technicians", tags=["Technicians"])

@router.post("/", response_model=TechnicianResponse)
def create_technician(data: TechnicianCreate, db: Session = Depends(get_db)):
    tech = Technician(
        name=data.name,
        mobile=data.mobile,
        work=data.work,
        description=data.description,
        rating=data.rating,
        image_url=data.image_url
    )
    db.add(tech)
    db.commit()
    db.refresh(tech)

    for sub_id in data.sub_category_ids:
        link = TechnicianSubCategory(technician_id=tech.id, sub_category_id=sub_id)
        db.add(link)
    db.commit()

    return get_technician_details(tech.id, db)

# @router.post("/by_ids/", response_model=list[TechnicianResponse])
# def get_technicians_by_ids(ids: list[int], db: Session = Depends(get_db)):
#     technicians = db.query(Technician).filter(Technician.id.in_(ids)).all()
#     return [get_technician_details(tech.id, db) for tech in technicians]

# # Helper to compose response
# def get_technician_details(tech_id: int, db: Session) -> TechnicianResponse:
#     tech = db.query(Technician).filter(Technician.id == tech_id).first()
#     if not tech:
#         raise HTTPException(status_code=404, detail="Technician not found")

#     sub_infos = []
#     cat_ids = set()
#     for link in tech.sub_category_links:
#         sub = db.query(SubCategory).filter(SubCategory.id == link.sub_category_id).first()
#         if sub:
#             sub_infos.append(SubCategoryInfo(
#                 id=sub.id,
#                 name=sub.name,
#                 category_id=sub.category_id,
#                 image_url=sub.image_url
#             ))
#             cat_ids.add(sub.category_id)

#     cat_infos = []
#     for cid in cat_ids:
#         cat = db.query(Category).filter(Category.id == cid).first()
#         if cat:
#             cat_infos.append(CategoryInfo(
#                 id=cat.id,
#                 name=cat.name,
#                 image_url=cat.image_url
#             ))

#     return TechnicianResponse(
#         id=tech.id,
#         name=tech.name,
#         mobile=tech.mobile,
#         work=tech.work,
#         description=tech.description,
#         rating=tech.rating,
#         image_url=tech.image_url,
#         sub_category_info=sub_infos,
#         category_info=cat_infos
#     )
