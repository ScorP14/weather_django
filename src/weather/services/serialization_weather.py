from datetime import datetime
from dataclasses import dataclass

import json

from .utils import convert_gradus_in_side_horizon
from ..schema import City, TemperatureData


@dataclass
class SerializationWeather:
    data: dict

    def get_city(self) -> City:
        return City.parse_obj(self.data['city'])

    def get(self):
        return [self.get_instance_temp(i) for i in self.data['list']]

    @staticmethod
    def get_instance_temp(item: dict) -> TemperatureData:
        return TemperatureData(
            date=datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S'),
            main_temp=item['main']['temp'],
            pressure=item['main']['pressure'],
            speed_wind=item['wind']['speed'],
            direction_wind=item['wind']['deg'],
            humidity=item['main']['humidity'],
        )

    def get_data_by_day(self):
        data_only_certain_times = [i for i in self.get() if i.date.time().hour in [3, 9, 15, 21]]
        response = {'city': self.get_city().dict()}
        result = {}
        for data in data_only_certain_times:
            key = data.date.date()
            if key not in result:
                result[key] = {}

            if data.date.time().hour == 3:
                result[key]['night'] = {
                    'temp': data.main_temp, 'pressure': data.pressure, 'speed': data.speed_wind,
                    'direction_speed': convert_gradus_in_side_horizon(data.direction_wind), 'humidity': data.humidity,
                    'str_dey': 'Ночь',
                }

            if data.date.time().hour == 9:
                result[key]['morning'] = {
                    'temp': data.main_temp, 'pressure': data.pressure, 'speed': data.speed_wind,
                    'direction_speed': convert_gradus_in_side_horizon(data.direction_wind), 'humidity': data.humidity,
                    'str_dey': 'Утро',
                }

            if data.date.time().hour == 15:
                result[key]['after_noon'] = {
                    'temp': data.main_temp, 'pressure': data.pressure, 'speed': data.speed_wind,
                    'direction_speed': convert_gradus_in_side_horizon(data.direction_wind), 'humidity': data.humidity,
                    'str_dey': 'Полдень',
                }

            if data.date.time().hour == 21:
                result[key]['evening'] = {
                    'temp': data.main_temp, 'pressure': data.pressure, 'speed': data.speed_wind,
                    'direction_speed': convert_gradus_in_side_horizon(data.direction_wind), 'humidity': data.humidity,
                    'str_dey': 'Вечер',
                }
        response['data'] = result
        return response
