from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import List, Optional
from enum import Enum

class LedChannel(str, Enum):
    IR = "ir"
    RED = "red"

class SensorReadingCreate(BaseModel):
    timestamp: datetime
    ir_value: int
    red_value: int
    heart_rate: Optional[float] = None  # bpm
    spo2: Optional[int] = None  # %
    temperature: Optional[float] = None  # °C

    @field_validator('ir_value', 'red_value')
    @classmethod
    def check_range(cls, v):
        if not 0 <= v <= 262143:
            raise ValueError('Value must be between 0 and 262143')
        return v

class SensorReadingOut(SensorReadingCreate):
    device_id: str
    id: str

class SensorBatch(BaseModel):
    device_id: str
    start_timestamp: datetime
    sample_rate: int
    readings: List[SensorReadingCreate]