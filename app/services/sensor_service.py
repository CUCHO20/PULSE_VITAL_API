from fastapi import HTTPException
from app.schemas.sensor import SensorBatch
from app.crud.sensor_crud import create_sensor_batch, get_readings_by_device
from typing import List
from app.models.sensor import SensorReading

async def process_sensor_batch(batch: SensorBatch) -> SensorBatch:
    if batch.sample_rate < 50 or batch.sample_rate > 3200:
        raise HTTPException(status_code=400, detail="Sample rate fuera de rango (50-3200 Hz)")
    
    inserted = await create_sensor_batch(batch)
    
    if len(inserted.inserted_ids) != len(batch.readings):
        raise HTTPException(status_code=500, detail="Error while inserting sensor readings")
    
    return batch

async def get_device_readings(device_id: str, limit: int = 10) -> List[SensorReading]:
    readings = await get_readings_by_device(device_id, limit)
    if not readings:
        raise HTTPException(status_code=404, detail="Don't found any readings for the specified device")
    return readings