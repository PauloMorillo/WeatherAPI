from django.urls import path, include
from rest_framework import routers
from webapi import views


urlpatterns = [
    path('weather', views.WeatherView.as_view())
]
