from django.test import TestCase
from utils.weather import WeatherService
from weather_api.settings import WEATHER_BASE_URL, WEATHER_APP_ID
from django.utils import timezone


class WeatherTestCase(TestCase):
    def setUp(self):
        self.weather = WeatherService("Bogota, co")

    def test_weather_constructor(self):
        """Checking constructor"""
        self.assertEqual(self.weather.app_id, WEATHER_APP_ID)
        self.assertEqual(self.weather.base_url, WEATHER_BASE_URL)
        self.assertEqual(self.weather.location, "q=Bogota, co")

    def test_get_relevant_data(self):
        """Testing readable format in response answer"""

        weather_result = {"coord": {"lon": -74.0817, "lat": 4.6097},
                          "weather": [{"id": 801, "main": "Clouds", "description": "few clouds", "icon": "02d"}],
                          "base": "stations",
                          "main": {"temp": 286.88, "feels_like": 285.93, "temp_min": 286.88, "temp_max": 286.88,
                                   "pressure": 1028, "humidity": 62}, "visibility": 10000,
                          "wind": {"speed": 2.06, "deg": 170}, "clouds": {"all": 20}, "dt": 1661434589,
                          "sys": {"type": 1, "id": 8582, "country": "CO", "sunrise": 1661424704, "sunset": 1661468731},
                          "timezone": -18000, "id": 3688689, "name": "Bogota", "cod": 200}

        response = self.weather.get_relevant_data(weather_result)

        readable_response = {
            "celsius_temperature": "13.73 ºC",
            "fahrenheit_temperature": "56.71 ºF",
            "wind": "2.06 m/s",
            "cloudiness": "few clouds",
            "pressure": "1028 hpa",
            "humidity": "62%",
            "sunrise": "10:51",
            "sunset": "23:05",
            "geo_coordinates": "[4.6097, -74.0817]",
            "requested_time": timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        for key, value in readable_response.items():
            self.assertEqual(response[key], value)

    def test_celsius_to_fahrenheit(self):
        """Checking celsius to fahrenheit"""
        fahrenheit = self.weather.celsius_to_fahrenheit(13.73)
        self.assertEqual(round(fahrenheit, 2), 56.71)

    def test_kelvin_to_celsius(self):
        """Checking kelvin to celsius"""
        celsius = self.weather.kelvin_to_celsius(286.88)
        self.assertEqual(round(celsius, 2), 13.73)
