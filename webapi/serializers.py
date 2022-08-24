from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    location_name = serializers.CharField()
    temperature = serializers.CharField()
    wind = serializers.CharField()
    cloudiness = serializers.CharField()
    pressure = serializers.CharField()
    humidity = serializers.CharField()
    sunrise = serializers.IntegerField()
    sunset = serializers.IntegerField()
    geo_coordinates = serializers.IntegerField()
    requested_time = serializers.IntegerField()
    forecast = serializers.JSONField()
