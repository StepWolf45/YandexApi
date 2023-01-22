import requests
import json

from config import Config 

def pressure_humidity():
    key = Config.get_weather_key()
    url = 'https://api.weather.yandex.ru/v2/forecast'  
    latitude = 55.777044
    longitude = 37.55555
    response = requests.get(
        url=url,
        params={
            'lat': latitude,
            'lon': longitude
        },
        headers={
            'X-Yandex-API-Key': key
        }
    )
    data = response.json()
    fact = data['fact']
    print(f"влажность: {fact['humidity']} %")
    print(f"давление: {fact['pressure_mm']} мм. рт. ст.")


if __name__ == '__main__':
    pressure_humidity()
