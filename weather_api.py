# -*-coding:utf-8 -*-
# File :weather_api.py
# Author:George
# Date : 2019/9/21
# motto: Someone always give up while someone always try!
"""
    weather api project
    urllib.parse to encode chinese
"""
import requests
from urllib import parse
import json


def weather_api():
    """
    sojson weather api changed we also need change
    天津市: 101030100

    :return:
    """
    city_code = str(input("Please enter the city code: "))
    url = 'http://t.weather.sojson.com/api/weather/city/' + city_code
    # city = str(input("Please enter the city code: "))
    # city_data = {'city_code': '101030100'}
    # city_data = parse.urlencode(city_data).encode('utf-8')
    response = requests.get(url)
    print(response.status_code)
    print(response.text)
    print(type(response.text))
    print(response.json())
    print(type(response.json()))

    # print(type(response.text))
    # print(type(response.json()))
    # response = response.json()
    # print("The message is '{}' ".format(response['message']))
    # print(response['date'])
    # print(response['cityInfo']['citykey'])
    # print(response['data']['forecast'][2]['fx'])
    # print(response['data']['yesterday'])
    # print(response['data']['yesterday']['week'])


if __name__ == "__main__":
    weather_api()