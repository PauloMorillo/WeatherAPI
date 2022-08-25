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

        location_name = f'{city},{country.upper()}'
        weather = WeatherService(location_name)
        result = weather.get_weather()
        adapted_result = WeatherService.get_relevant_data(result)
        adapted_result["location_name"] = location_name
        serialized_data = WeatherSerializer(adapted_result)

        return Response(serialized_data.data)
