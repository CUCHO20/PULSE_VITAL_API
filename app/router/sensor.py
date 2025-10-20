from fastapi import APIRouter, Depends, HTTPException
from app.schemas.sensor import SensorBatch
from app.services.sensor_service import process_sensor_batch, get_device_readings
from app.models.sensor import SensorReading
from app.core.config import get_db_init
from typing import List

router = APIRouter(prefix="/sensor", tags=["sensor"])

@router.post("/readings", response_model=SensorBatch)
async def receive_readings(batch: SensorBatch, db_init: None = Depends(get_db_init)):
    return await process_sensor_batch(batch)

@router.get("/readings/{device_id}", response_model=List[SensorReading])
async def get_readings(device_id: str, limit: int = 10, db_init: None = Depends(get_db_init)):
    return await get_device_readings(device_id, limit)