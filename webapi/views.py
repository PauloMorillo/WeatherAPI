from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.weather import WeatherService
from .serializers import WeatherSerializer


class WeatherView(APIView):

    def get(self, request, format=None):
        """
        Return the weather according to the city and country params
        """
        city = self.request.query_params.get('city')
        country = self.request.query_params.get('country')

        weather = WeatherService(f'{city},{country}')
        result = weather.get_weather()

        return Response(result)
