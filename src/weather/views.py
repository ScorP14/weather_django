from django.shortcuts import render

from .services.client_weather import WeatherApiClient
from .services.serialization_weather import SerializationWeather


def weather_seven_dey(request, city_name: str):
    from config.constant import ConstantFromEnv
    result = {}
    try:
        client_weather = WeatherApiClient(ConstantFromEnv().owm_api_key)
        result = SerializationWeather(client_weather.get_forecast_by_city_name(city_name)).get_data_by_day()
    except Exception as e:
        print(e)
        result['error'] = 'Ошибка сервера, попробуйте снова'
    return render(request, 'main_page.html', context=result)
