import requests
from config import Config
def wind_speed_direction():
    key = Config.get_weather_key()
    url = 'https://api.weather.yandex.ru/v2/forecast'      # если тестовый аккаунт
    latitude = 63.464489
    longitude = 142.789134
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
            if 'application/json' in response.headers['Content-Type']:
                data = response.json()
                fact = data['fact']
                nap = []
                rusnap = []
                if fact['wind_dir'] == "nw":
                    nap = "↖"
                    rusnap = "северо-западное"
                elif fact['wind_dir'] == "n":
                    nap = "↑"
                    rusnap = "северное"
                elif fact['wind_dir'] == "ne":
                    nap = "↗"
                    rusnap = "северо-восточное"
                elif fact['wind_dir'] == "e":
                    nap = "→"
                    rusnap = "восточное"
                elif fact['wind_dir'] == "se":
                    nap = "↘"
                    rusnap = "юго-восточное"
                elif fact['wind_dir'] == "s":
                    nap = "↓"
                    rusnap = "южное"
                elif fact['wind_dir'] == "sw":
                    nap = "↙"
                    rusnap = "юго-западное"
                elif fact['wind_dir'] == "w":
                    nap = "←"
                    rusnap = "западное"
                elif fact['wind_dir'] == "c":
                    nap = "s"
                    rusnap = "штиль"
                print("Погода в городе Москва")
                print(f"Сила ветра: {fact['wind_speed']} м/с")
                print(f"Направление ветра:  {nap, rusnap}")
            else:
                print('415 - Ошибка, ожидался документ в формате json')
        elif response.status_code == 403:
            print('403 - доступ запрещен / forgebidden')
        else:
            print('520 - неизвестная ошибка')
    except requests.exceptions.ConnectionError:
        print('522 - ошибка подключения интернета')


if __name__ == '__main__':
    wind_speed_direction()
