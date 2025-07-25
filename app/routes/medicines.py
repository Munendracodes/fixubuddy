from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from app.schemas import medicine as schemas_medicine, drug as schemas_drug
from app.models.medicines import Medicine
from app.models.drugs import Drug# Assuming these models exist
from app.database import get_db  # Assuming a database session is managed here
from sqlalchemy.orm import Session
from app.schemas.pagination import get_pagination, PaginationParams
from sqlalchemy import func, or_

router = APIRouter(
    prefix="/medicines",
    tags=["Medicines"],
    responses={404: {"description": "Not found"}},
)

@router.get("/Search", response_model=List[schemas_medicine.MedicineRead])
async def search_medicines(
    q: str = Query(..., description="Search by medicine or drug name"),
    db: Session = Depends(get_db)):
    
    query = db.query(Medicine).join(Medicine.drugs).filter(
    or_(
        Medicine.name.ilike(f"%{q}%"),
        Drug.name.ilike(f"%{q}%")
        )
    ).distinct()
    return query.all()

@router.get("/", summary="List all medicines", 
            description="Returns a paginated list of all available medicines in stock.", 
            response_model=schemas_medicine.PaginatedMedicineRead, include_in_schema=False)
async def list_medicines(db: Session = Depends(get_db),
    pagination: PaginationParams = Depends(get_pagination)):
    skip = pagination.skip
    limit = pagination.limit
    
    total = db.query(func.count(Medicine.id)).scalar()
    items = db.query(Medicine).offset(skip).limit(limit).all()
    next_skip = skip + limit if skip + limit < total else None
    
    return {
        "medicines": items,
        "total": total,
        "skip": skip,
        "limit": limit,
        "next_skip": next_skip
    }

@router.post(
    "/",
    summary="Add new medicine with drug names",
    description="Insert a new medicine and auto-create or assign drugs by name.",
    response_model=schemas_medicine.MedicineRead
)
async def create_medicine(medicine: schemas_medicine.MedicineCreate, db: Session = Depends(get_db)):
    print("🚀 Received request to add new medicine")
    print(f"📦 Medicine Data: {medicine.dict()}")

    drug_objs = []
    for drug_name in medicine.drugs:
        normalized_name = drug_name.strip().title()
        print(f"🔍 Checking drug: '{normalized_name}'")

        existing_drug = db.query(Drug).filter(Drug.name == normalized_name).first()
        if existing_drug:
            print(f"✅ Found existing drug: {existing_drug.name} (ID: {existing_drug.id})")
            drug_objs.append(existing_drug)
        else:
            print(f"🆕 Creating new drug: {normalized_name}")
            new_drug = Drug(name=normalized_name)
            db.add(new_drug)
            db.flush()
            print(f"🎉 New drug added with ID: {new_drug.id}")
            drug_objs.append(new_drug)

    # Create medicine without drug names
    med_data = medicine.dict(exclude={"drugs"})
    db_medicine = Medicine(**med_data)
    db_medicine.drugs = drug_objs

    print("💾 Saving medicine to database...")
    db.add(db_medicine)
    db.commit()
    db.refresh(db_medicine)

    print(f"✅ Medicine '{db_medicine.name}' added successfully with ID: {db_medicine.id}")
    print("🧪 Associated drugs:", [drug.name for drug in drug_objs])

    return db_medicine



@router.get("/{medicine_id}", summary="Get medicine", description="Fetch a medicine by its ID.", response_model=schemas_medicine.MedicineRead, include_in_schema=False)
async def get_medicine(medicine_id: int, db: Session = Depends(get_db)):
    if medicine_id == 0:
        raise HTTPException(status_code=404, detail="Medicine not found")
    db_medicine = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if not db_medicine:
        raise(HTTPException(status_code=404, detail="Medicine Not Found"))
    return db_medicine

@router.put("/{medicine_id}", summary ="Update Medicine Status", description = "If the Medicine is Active it will Deactivate, If the Medicine is Deactive Status it will Activate")
async def update_medicine_status(medicine_id: int, status: int | None = 1, db: Session = Depends(get_db)):
    medicine_info = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if not medicine_info:
        raise HTTPException(status_code=404, detail="Medicine not Found")
    medicine_info.status = status
    db.add(medicine_info)
    db.commit()
    message = "Medicine Activated" if status == 1 else "Medicine Dectivated"
    return {"medicine_id": medicine_id, "message": message}
    
    