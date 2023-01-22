from config import Config
from speller.menu import speller_menu
from weather_forecast.menu import weather_forecast_menu
from current_weather.menu import current_weather_menu

def main():
    Config.load_config()
    print('1. Текущая погода\n2. Прогноз погоды\n3. Проверка правописания\n4. Безопасность ссылок\n0. Выход\n')
    choice = int(input())
    if(choice == 1):
        current_weather_menu()
    elif(choice == 2):
        weather_forecast_menu()
    elif(choice == 3):
        print('speller')
        speller_menu()
    elif(choice == 4):
        print('safe_browsing')
        #safe_browsing()
    elif(choice == 0):
        pass

if __name__ == '__main__':
    main()
