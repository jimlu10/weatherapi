# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import requests

from rest_framework import serializers

@api_view(['POST'])
def get_city_weather_info(request):
    """
    Recieves a city name to return the coordinates
    :param latitude: City's latitude
    :param longitude: City's longitude
    :return: City coordinates
    """
    city_name = request.POST.get('city_name')
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric' % (city_name, settings.APP_ID))
    try:
        if response.status_code == 200:
            info = response.json()
            json_response = {
                'name': info['name'], 'temp': info['main']['temp'],
                'latitude': info['coord']['lat'], 'longitude': info['coord']['lon'],
            }
        else:
            json_response = {'error': 'Error on getting data'}
    except:
        json_response = {'error': 'Problem on request weather information'}
    return Response(json_response)
