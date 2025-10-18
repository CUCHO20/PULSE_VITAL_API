from beanie import Document, Indexed
from app.schemas.sensor import SensorReading as SensorSchema


class SensorReading(Document, SensorSchema):
    device_id: str = Indexed()

    class Settings:
        name = "sensor_readings"
        indexes = [
            "device_id",
            "timestamp",
        ]