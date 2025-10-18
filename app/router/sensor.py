from fastapi import APIRouter
from app.schemas.sensor import SensorBatch
from app.models.sensor import SensorReading
from app.services.sensor_service import get_device_readings, process_sensor_batch

router = APIRouter(prefix="/sensor", tags=["sensor"])

@router.post("/readings", response_model=SensorBatch)
async def receive_readings(batch: SensorBatch):
    return await process_sensor_batch(batch)

@router.get("/readings/{device_id}", response_model=list[SensorReading])
async def get_readings(device_id: str, limit: int = 10):
    return await get_device_readings(device_id, limit)