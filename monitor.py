from fastapi import APIRouter, Depends, HTTPException
from app.models import Event
from app.database import events_collection
from app.auth import verify_token

router = APIRouter()

@router.post("/log")
def log_event(event: Event, user=Depends(verify_token)):
    if event.cpu_usage > 80 or event.memory_usage > 90:
        # Alert triggered
        print("⚠️ Alert: High usage detected")
    
    events_collection.insert_one(event.dict())
    return {"message": "Event logged"}
