from datetime import datetime
from typing import Optional
from beanie import Document, Indexed
from app.schemas.sensor import SensorReading as SensorSchema


class SensorReading(Document, SensorSchema):
    device_id: str = Indexed()
    timestamp: datetime
    ir_value: int
    red_value: int
    heart_rate: Optional[float] = None
    spo2: Optional[int] = None
    temperature: Optional[float] = None

    class Settings:
        name = "sensor_readings"