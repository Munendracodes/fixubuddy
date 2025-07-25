# app/models/compositions.py
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database import Base

# Join table: medicine_id <-> drug_id
compositions = Table(
    "compositions",
    Base.metadata,
    Column("medicine_id", ForeignKey("medicines.id"), primary_key=True),
    Column("drug_id", ForeignKey("drugs.id"), primary_key=True)
)
