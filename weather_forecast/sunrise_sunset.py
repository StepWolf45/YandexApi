import json
import os

import requests


def get_api_key():
    if not os.path.exists('config.json'):
        config_file = open('config.json', 'w')
        data = {"key": "DEFINE ME!"}
        json.dump(data, config_file, indent=4)
        config_file.close()
        raise RuntimeError('Ошибка: конфиг-файл не существует. Создаю пустым, но ключа там нет')

    config_file = open('config.json')
    data = json.load(config_file)

    try:
        key = data['key']
    except KeyError:
        print('Ошибка: не найден ключ API')
        key = None

    config_file.close()
    return key


def sunrise_sunset():
    key = get_api_key()
    # url = 'https://api.weather.yandex.ru/v2/informers'     # если бесплатный аккаунт
    url = 'https://api.weather.yandex.ru/v2/forecast'      # если тестовый аккаунт
    latitude = 55.7522200
    longitude = 37.6155600
    try:
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
        if response.status_code == 200:
            print('Ok')
            if 'application/json' in response.headers['Content-Type']:
                data = response.json()
                forecasts = data['forecasts']
                print(f"Темпе.ратура (По ощущениям): {forecasts[1,'sunrise']}")
                print(f"Температура: {forecasts[1,'sunset']}")
            else:
                print('Ошибка, ожидался документ в формате json')
        elif response.status_code == 403:
            print('Forbidden')
        else:
            print('Error')
    except requests.exceptions.ConnectionError:
        print('Кажется, нет интернета')


if __name__ == '__main__':
    sunrise_sunset()
