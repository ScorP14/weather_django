from dataclasses import dataclass
from datetime import datetime
from typing import Any

from pydantic import BaseModel, field_validator


@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

    def to_dict(self):
        return dict(lat=self.lat, lon=self.lon)


class TemperatureData(BaseModel):
    date: datetime
    main_temp: float
    pressure: int
    speed_wind: float
    direction_wind: int
    humidity: int

    @field_validator('pressure')
    @classmethod
    def validate(cls, value: Any):
        """Из Паскалей в мм. рт. ст."""
        return int(value / 1.33)


class City(BaseModel):
    id: int
    name: str
    country: str
    coord: Coordinate
