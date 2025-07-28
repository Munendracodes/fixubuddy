# app/api/address.py
import os
import httpx
from fastapi import APIRouter, Query, HTTPException
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

router = APIRouter(
    prefix="/address",
    tags=["Address"]
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

@router.get("/get-address")
async def get_address(lat: float = Query(...), lon: float = Query(...)):
    if not GOOGLE_API_KEY:
        raise HTTPException(status_code=500, detail="Google API key not configured")

    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "latlng": f"{lat},{lon}",
        "key": GOOGLE_API_KEY
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        data = response.json()

    if data["status"] == "OK" and data["results"]:
        address = data["results"][0]["formatted_address"]
        return {"address": address}
    else:
        raise HTTPException(status_code=404, detail="Address not found")
