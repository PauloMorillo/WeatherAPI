from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    location_name = serializers.CharField()
    celsius_temperature = serializers.CharField()
    fahrenheit_temperature = serializers.CharField()
    wind = serializers.CharField()
    cloudiness = serializers.CharField()
    pressure = serializers.CharField()
    humidity = serializers.CharField()
    sunrise = serializers.CharField()
    sunset = serializers.CharField()
    geo_coordinates = serializers.CharField()
    requested_time = serializers.CharField()
