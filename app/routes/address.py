# app/api/address.py
from fastapi import APIRouter, Query, HTTPException
from opencage.geocoder import OpenCageGeocode

router = APIRouter(
    prefix="/address",
    tags=["Address"]
)

@router.get("/get-address")
def get_address(lat: float = Query(...), lon: float = Query(...)):
    key = "7f906e21c8b14fad8777c1551d40b7f0"
    geocoder = OpenCageGeocode(key)
    result = geocoder.reverse_geocode(lat, lon)
    if result and len(result):
        return {"address": result[0]['formatted']}
    else:
        raise HTTPException(status_code=404, detail="Address not found")

