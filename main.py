import requests
import json
import pandas

url = 'http://api.weatherapi.com/v1/forecast.json?key=934bee22e81541bc893165903212004&q=91606&days=1&aqi=no&alerts=no'
request = requests.get(url)
response = request.json()

weather_dict = dict(response)

def current_temp(dic):
    current = dic['current']
    current_time = current['last_updated']
    current_temp = current['temp_f']
    current_feel = current['feelslike_f']
    uv = current['uv']

    return current_time, current_temp, current_feel, uv, gust

print('Current Temp: ', current_temp(weather_dict))
