from datetime import datetime
from typing import Optional
from beanie import Document, Indexed
from pydantic import Field

class SensorReading(Document):
    device_id: str = Indexed()
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    ir_value: int
    red_value: int
    heart_rate: Optional[float] = None
    spo2: Optional[int] = None
    temperature: Optional[float] = None

    class Settings:
        name = "sensor_readings"