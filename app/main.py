from fastapi import FastAPI
from app.routes.medicines import router as medicines_router
from app.routes.drugs import router as drugs_router
from app.database import engine
from app.models.medicines import Base
from app.models import drugs, compositions, medicines


app = FastAPI(
    title="Pharmacy Management API 🧪💊",
    description="Manage medicines, drugs, stock and more 🚀",
    version="1.0.0",
    docs_url="/docs",              # Swagger UI path
    redoc_url="/redoc",            # ReDoc path
    openapi_url="/openapi.json",   # OpenAPI spec path
)

# Create all tables from models
Base.metadata.create_all(bind=engine)

app.include_router(drugs_router, include_in_schema=False)
app.include_router(medicines_router)
