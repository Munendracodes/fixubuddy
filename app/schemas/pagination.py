from fastapi import Query
from pydantic import BaseModel

class PaginationParams(BaseModel):
    skip: int = Query(0, ge=0)
    limit: int = Query(10, ge=1, le=100)

def get_pagination(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)) -> PaginationParams:
    return PaginationParams(skip=skip, limit=limit)
