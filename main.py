import requests

city = ("Moscow,RU")
apiKey = open("apiKey.txt").readline()

weatherJSON = requests.get(f"http://api.openweathermap.org/data/2.5/weather",
                           params={"appid": apiKey, "q": city, "units": "metric", "lang": "ru"}).json()

forecastJSON = requests.get(f"http://api.openweathermap.org/data/2.5/forecast",
                            params={"appid": apiKey, "q": city, "units": "metric", "lang": "ru"}).json()["list"]

print(f"""Погода в городе {city}
    Погодные условия: {weatherJSON["weather"][0]["description"]}
    Температура: {weatherJSON["main"]["temp"]}
    Минимальная температура: {weatherJSON["main"]["temp_min"]}
    Максимальная температура: {weatherJSON["main"]["temp_max"]}
    Скорость ветра: {weatherJSON["wind"]["speed"]} м/сек
    Видимость: {weatherJSON["visibility"]}
_____________________________________________""")

for i in forecastJSON:
    print(f"""Погода на {i["dt_txt"]}
    Погодные условия: {i["weather"][0]["description"]}
    Температура: {i["main"]["temp"]}
    Минимальная температура: {i["main"]["temp_min"]}
    Максимальная температура: {i["main"]["temp_max"]}
    Скорость ветра: {i["wind"]["speed"]} м/сек
    Видимость: {i["visibility"]}
_____________________________________________""")
