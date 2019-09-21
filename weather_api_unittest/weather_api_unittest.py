# -*-coding:utf-8 -*-
# File :weather_api_unittest.py
# Author:George
# Date : 2019/9/21
# motto: Someone always give up while someone always try!
"""
    unittest to complete weather api test!
        1. test case method in unittest must starts with test

"""

import unittest
import requests
# from urllib import parse
import time


class WeatherTest(unittest.TestCase):
    """Weather Api Interface Test"""

    def setUp(self):
        self.url = 'http://t.weather.sojson.com/api/weather/city/'

    def test_tianjing_correct_param(self):
        city_code = '101030100'
        # if there is chinese in your query sting  use parse to encode
        # data = {'city': '天津'}
        # city = parse.urlencode(data).encode('utf-8')
        response = requests.get(self.url + city_code)
        result = response.json()

        self.assertEqual(result['status'], 200)
        self.assertEqual(result['cityInfo']['city'], '天津市')
        self.assertEqual(result['cityInfo']['citykey'], '101030100')
        time.sleep(3)

    def test_tianjing_param_wrong(self):
        city_code = '21312343'
        response = requests.get(self.url + city_code)
        result = response.json()
        # self.assertNotEqual(result['status'], 200)
        self.assertEqual(result['status'], 404)
        self.assertEqual(result['message'], 'Request resource not found.')
        time.sleep(3)

    def test_weather_param_blank(self):
        city_code = ''
        response = requests.get(self.url + city_code)
        result = response.json()
        self.assertEqual(result['status'], 404)
        self.assertEqual(result['message'], 'Request resource not found.')
        time.sleep(3)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
