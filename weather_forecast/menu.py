from weather_forecast.pressure_humidity import pressure_humidity


def weather_forecast_menu():
    print('''1. время восхода и заката солнца
2. минимальная и максимальная температура
3. влажность и давление
4. тип осадков
0. назад''')
    cmdNum = int(input())

    if cmdNum == 1:
        print('sunrise_sunset')
    elif cmdNum == 2:
        print('max_min_temp')
    elif cmdNum == 3:
        pressure_humidity()
    elif cmdNum == 4:
        print('prec_type')


if __name__ == '__main__':
    weather_forecast_menu()
