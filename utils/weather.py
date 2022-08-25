import datetime

from django.utils import timezone
from rest_framework.exceptions import APIException
import requests


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
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                raise APIException("In this moment our server is not working as expected, please try in few seconds")
        except requests.exceptions.RequestException as e:
            raise APIException("In this moment our server is not working as expected, please try in few seconds")

    @staticmethod
    def get_relevant_data(result):
        """
        This method gets the attributes required in response
        """
        celsius = round(WeatherService.kelvin_to_celsius(float(result["main"]["temp"])), 2)
        celsius_temperature = f'{celsius} ºC'
        fahrenheit_temperature = f'{round(WeatherService.celsius_to_fahrenheit(celsius), 2)} ºF'
        wind = result["wind"]["speed"]
        cloudiness = result["weather"][0]["description"]
        pressure = f'{result["main"]["pressure"]} hpa'
        humidity = f'{result["main"]["humidity"]}%'
        sunrise = datetime.datetime.fromtimestamp(result["sys"]["sunrise"]).strftime("%H:%M")
        sunset = datetime.datetime.fromtimestamp(result["sys"]["sunset"]).strftime("%H:%M")
        geo_coordinates = f'[{result["coord"]["lat"]}, {result["coord"]["lon"]}]'

        result = {
            "location_name": "location_name",
            "celsius_temperature": celsius_temperature,
            "fahrenheit_temperature": fahrenheit_temperature,
            "wind": f"{wind} m/s",
            "cloudiness": cloudiness,
            "pressure": pressure,
            "humidity": humidity,
            "sunrise": sunrise,
            "sunset": sunset,
            "geo_coordinates": geo_coordinates,
            "requested_time": timezone.now().strftime("%Y-%m-%d, %H:%M:%S")

        }

        return result

    @staticmethod
    def celsius_to_fahrenheit(celsius_weather=0):
        """
        This method converts celsius to fahrenheit
        :param: celsius_weather  weather in celsius degrees
        type:
        """
        return (celsius_weather * (9 / 5)) + 32

    @staticmethod
    def kelvin_to_celsius(kelvin=0):
        """
        This method converts kelvin to celsius
        :param: celsius_weather  weather in celsius degrees
        type:
        """
        return kelvin - 273.15
