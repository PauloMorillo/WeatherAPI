import requests
import json


class WeatherService:

    def __init__(self, location_name):
        self.app_id = '1508a9a4840a5574c822d70ca2132032'
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather?'
        self.location = f'q={location_name}'

    def get_weather(self):
        """
        This method returns the weather service response
        :return: service response in json format
        """
        url = f'{self.base_url}{self.location}&appid={self.app_id}'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def change_weather_to_fahrenheit(celsius_weather=0):
        """
        This method converts celsius to fahrenheit
        :param: celsius_weather  weather in celsius degrees
        type:
        """
        return (int(celsius_weather) * (9 / 5)) + 32
