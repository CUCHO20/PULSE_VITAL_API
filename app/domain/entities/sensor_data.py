import datetime
from typing import Optional
from pydantic import BaseModel, Field

class SensorData(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    temperature: float = Field(..., ge=-40, le=80, description="°C Temperature")
    humidity: float = Field(..., ge=-0, le=100, description="% Humidity")
    sensor_id: str = Field(..., description="ESP32 Sensor identificator")
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "temperature": 25.5,
                "humidity": 60.0,
                "sensor_id": "ESP32_001"
            }
        }