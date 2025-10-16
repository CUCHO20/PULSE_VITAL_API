from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional

from app.domain.entities.sensor_data import SensorData


class SensorRepository(ABC):
    @abstractmethod
    async def create(self, sesnor_data: SensorData) -> SensorData:
        pass

    @abstractmethod
    async def get_all(self, limit: int = 1000) -> List[SensorData]:
        pass

    @abstractmethod
    async def get_by_sensor_id(self, sensor_id:str, limit:int = 1000) -> List[SensorData]:
        pass

    @abstractmethod
    async def get_data_by_range(
        self,
        start_date:datetime,
        end_date:datetime,
        sensor_id: Optional[str] = None
    ) -> List[SensorData]:
        pass