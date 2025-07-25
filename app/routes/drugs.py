from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from app.schemas import medicine as schemas_medicine, drug as schemas_drug
from app.models.medicines import Medicine
from app.models.drugs import Drug# Assuming these models exist
from app.database import get_db  # Assuming a database session is managed here
from sqlalchemy.orm import Session
from app.schemas.pagination import get_pagination, PaginationParams
from sqlalchemy import func

router = APIRouter(
    prefix="/Drugs",
    tags=["Drugs"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=schemas_drug.PaginatedDrugRead)
async def get_drug_list(db: Session = Depends(get_db),
    pagination: PaginationParams = Depends(get_pagination)):
    skip = pagination.skip
    limit = pagination.limit
    
    total = db.query(func.count(Drug.id)).scalar()
    items = db.query(Drug).offset(skip).limit(limit).all()
    next_skip = skip + limit if skip + limit < total else None
    
    return {
        "drugs": items,
        "total": total,
        "skip": skip,
        "limit": limit,
        "next_skip": next_skip
    }
    
@router.post("/")
async def insert_all_drugs(
    payload: schemas_drug.DrugListCreate,
    db: Session = Depends(get_db)
):
    inserted = []
    for drug_data in payload.drugs:
        existing = db.query(Drug).filter(Drug.name == drug_data.name).first()
        if not existing:
            new_drug = Drug(name=drug_data.name)
            db.add(new_drug)
            inserted.append(drug_data.name)
    db.commit()
    return {"inserted": inserted, "message": f"{len(inserted)} drugs inserted."}
    
