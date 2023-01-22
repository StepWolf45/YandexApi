import requests
from config import Config


def pressure_humidity():
    Config.load_config()
    key = Config.get_weather_key()
    coords = [55.755864, 37.617698]

    address = 'https://api.weather.yandex.ru/v2/forecast'
    getparams = {
        'lat': coords[0],
        'lon': coords[1]
    }
    headers = {
        'X-Yandex-API-Key': key
    }

    response = requests.get(url=address, params=getparams, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print('Погода в городе Москва:')
        print('- Влажность: {}%'.format(data['fact']['humidity']))
        print('- Давление: {} мм рт. ст.'.format(data['fact']['pressure_mm']))
    else:
        print(response.status_code)


if __name__ == '__main__':
    pressure_humidity()
