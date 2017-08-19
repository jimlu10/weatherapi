# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from requests.auth import HTTPBasicAuth
from django.conf import settings
import simplejson
import requests


def index(request):
    return render(request, 'index/index.html', {})

def send_data(request):
    if request.method == 'POST':
        name = request.POST.get('city_name')
        params = requests.post(
            'http://localhost:8002/temp/',
            auth=HTTPBasicAuth(settings.API_USER, settings.API_PASS),
            data={'city_name': name}
        )
        if params.status_code == 200:
            return render(request, 'index/response.html', {'params': params.json(), 'maps_api_key': settings.MAPS_API_KEY})
    return HttpResponseBadRequest(simplejson.dumps({"error": 'No se puede procesar'}))