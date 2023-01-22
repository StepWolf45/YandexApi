import requests
import json

def temp_feels_like():
    key = "3d32272f-2da9-489b-88c0-fc86bd6ea7dc"
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
    print('Погода в городе Москва:')
    print(f"Температура: {fact['temp']}")
    print(f"Ощущается, как {fact['feels_like']}")


if __name__ == '__main__':
    temp_feels_like()
