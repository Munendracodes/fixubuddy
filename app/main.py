from fastapi import FastAPI
from app.routes.medicines import router as medicines_router
from app.routes.drugs import router as drugs_router
from app.database import engine
from app.models.medicines import Base
from app.models import drugs, compositions, medicines
from app.routes.users import router as users_router


from fastapi import FastAPI

from fastapi import FastAPI

app = FastAPI(
    title="🔧 FixuBuddy API🤝",
    description=(
        "📱 A mobile platform to connect customers with trusted service providers "
        "like 🧰 electricians, ❄️ AC technicians, 🚽 plumbers, and more – across your town! 🏡\n\n"
        "🗺️ Location-based suggestions, 🔐 OTP login, and 🛠️ reliable service management."
    ),
    version="1.0.0 🚀",
    docs_url="/docs",              # 📘 Swagger UI
    redoc_url="/redoc",            # 📕 ReDoc
    openapi_url="/openapi.json",   # 📄 OpenAPI schema
)



# Create all tables from models
Base.metadata.create_all(bind=engine)
app.include_router(users_router)
app.include_router(drugs_router, include_in_schema=False)
app.include_router(medicines_router)
