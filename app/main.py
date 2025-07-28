from fastapi import FastAPI
from app.database import engine
from app.routes.users import router as users_router
from app.routes.address import router as address_router
from app.routes.categories import router as category_router
from app.routes.sub_categories import router as sub_category_router
from app.routes.technician import router as technician_router
from app.models.users import Base
from fastapi.staticfiles import StaticFiles
import os

from fastapi import FastAPI

app = FastAPI(
    title="🔧 FixuBuddy API🤝",
    description=(
        ""
    ),
    version="1.0.0 🚀",
    docs_url="/docs",              # 📘 Swagger UI
    redoc_url="/redoc",            # 📕 ReDoc
    openapi_url="/openapi.json",   # 📄 OpenAPI schema
)

app.mount("/static", StaticFiles(directory=os.path.join("app", "static")), name="static")

# Create all tables from models
Base.metadata.create_all(bind=engine)
app.include_router(users_router, include_in_schema=False)

app.include_router(category_router)
app.include_router(sub_category_router)
app.include_router(technician_router)
app.include_router(address_router)
