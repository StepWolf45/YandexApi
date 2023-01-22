from current_weather.temp_feels_like import temp_feels_like
from current_weather.pressure_humidity import pressure_humidity
from current_weather.wind_speed_direction import wind_speed_direction

def current_weather_menu():
     print("""
        1. температура реальная и ощущаемая
        2. влажность и давление
        3. состояние погоды за окном
        4. скорость и направление ветра
        0. Назад
        """)
     answer = int(input())
     if answer == 1:
         temp_feels_like()
     elif answer == 2:
         pressure_humidity()
     elif answer == 3:
         print("condition")
     elif answer == 4:
         wind_speed_direction()
     elif answer == 0:
         exit()

if __name__ == '__main__':
    current_weather_menu()
