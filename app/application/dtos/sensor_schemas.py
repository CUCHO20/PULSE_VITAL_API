from pydantic import BaseModel, Field


class SensorDataCreate(BaseModel):
    temperature: float = Field(..., ge=-40, le=80)
    humidity: float = Field(..., ge=0, le=100)
    sensor_id: str = Field(..., min_length=1)