import requests
from Temperature_Parser_token import *
s_city = "Moscow,RU"
hgp = 0.75006375541921

def msc_weather_now():

    url = f'http://api.openweathermap.org/data/2.5/weather'
    global s_city
    global appid

    r = requests.get(url, params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = r.json()
    pressure = int(data['main']['pressure']) * hgp

    print(s_city)
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
    print("pressure:", pressure)

def msc_weather_5days_every3hours():
    url = f'http://api.openweathermap.org/data/2.5/forecast'
    global s_city
    global appid

    r = requests.get(url, params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = r.json()

    print(s_city)
    for date in data['list']:
        print(date['dt_txt'], '{0:+3.0f}'.format(date['main']['temp']), date['weather'][0]['description'])


msc_weather_now()
#msc_weather_5days_every3hours()
