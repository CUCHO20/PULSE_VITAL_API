from typing import List, Optional
from app.models.sensor import SensorReading
from app.schemas.sensor import SensorBatch

async def create_sensor_batch(batch: SensorBatch) -> List[SensorReading]:
    readings_instances = [
        SensorReading(
            device_id=batch.device_id,
            **reading.model_dump()
        )
        for reading in batch.readings
    ]
    inserted = await SensorReading.insert_many(readings_instances)
    return inserted

async def get_readings_by_device(device_id: str, limit: int = 10) -> List[SensorReading]:
    return await SensorReading.find({"device_id": device_id}).limit(limit).to_list()

async def get_latest_reading(device_id: str) -> Optional[SensorReading]:
    return await SensorReading.find({"device_id": device_id}).sort({"timestamp": -1}).first_or_none()