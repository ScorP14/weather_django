import json
from dataclasses import dataclass

import requests

from ..schema import Coordinate


@dataclass
class WeatherApiClient:
    api_key: str

    def __post_init__(self):
        self.check_connect()
        self.url_template_get_coord_by_city_name = 'https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=3'
        self.url_template_get_weather_city_name = 'https://api.openweathermap.org/data/2.5/weather?q={city}'
        self.url_template_get_forecast_city_name = 'https://api.openweathermap.org/data/2.5/forecast?q={city}'

    def check_connect(self):
        url = 'https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99'
        response = self._request(url)
        if response['cod'] != 200:
            raise Exception(response['message'])

    def get_coordinate_by_city_name(self, city_name: str) -> Coordinate | None:
        url = self.url_template_get_coord_by_city_name.format(city=city_name)
        response = self._request(url)
        return Coordinate(
            lat=response[0]['lat'],
            lon=response[0]['lon'],
        ) if response else None

    def _request(self, url: str):
        response = requests.get(url, params={'appid': self.api_key, 'units': 'metric', 'lang': 'ru'}, timeout=60)
        return json.loads(response.text)

    def get_weather_by_city_name(self, city_name: str):
        url = self.url_template_get_weather_city_name.format(city=city_name)
        return self._request(url)

    def get_forecast_by_city_name(self, city_name: str):
        url = self.url_template_get_forecast_city_name.format(city=city_name)
        response = self._request(url)
        return response

