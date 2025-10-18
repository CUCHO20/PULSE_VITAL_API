from typing import List, Optional
from app.models.sensor import SensorReading
from app.schemas.sensor import SensorBatch

async def create_sensor_batch(batch: SensorBatch) -> List[SensorReading]:
    """Inserta un lote de lecturas."""
    # ¡Cambio clave! Crea instancias de SensorReading en lugar de dicts
    readings_instances = [
        SensorReading(
            device_id=batch.device_id,
            **reading.model_dump()  # Desempaqueta los campos del esquema
        )
        for reading in batch.readings
    ]
    inserted = await SensorReading.insert_many(readings_instances)
    return inserted

async def get_readings_by_device(device_id: str, limit: int = 10) -> List[SensorReading]:
    """Obtiene lecturas recientes por dispositivo."""
    return await SensorReading.find(SensorReading.device_id == device_id).limit(limit).to_list()

async def get_latest_reading(device_id: str) -> Optional[SensorReading]:
    """Última lectura."""
    return await SensorReading.find(SensorReading.device_id == device_id).sort(-SensorReading.timestamp).first_or_none()