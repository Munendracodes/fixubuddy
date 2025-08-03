from fastapi import FastAPI
from app.database import engine
from app.routes.users import router as users_router
from app.routes.categories import router as category_router
from app.routes.sub_categories import router as sub_category_router
from app.routes.technician import router as technician_router
from app.models.categories import Base
# from fastapi.staticfiles import StaticFiles
import os
import uvicorn

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

# app.mount("/static", StaticFiles(directory=os.path.join("app", "static")), name="static")


# @app.get("/")
# def read_root():
#     return {"message": "FixuBuddy is running!"}

# Create all tables from models
Base.metadata.create_all(bind=engine)
app.include_router(users_router, include_in_schema=False)

app.include_router(category_router)
app.include_router(sub_category_router)
app.include_router(technician_router)



# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8080))
#     uvicorn.run("app.main:app", host="0.0.0.0", port=port)

