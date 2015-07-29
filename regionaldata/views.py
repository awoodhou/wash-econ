from django.http import HttpResponse
from django.shortcuts import render
import requests


def index(request):
    # Request available categories from BEA API (start w/ 'RegionalData')
    api_url = 'http://bea.gov/api/data/'
    params = {
        'UserID': '4ED778EA-6730-455D-8C60-1DE273F8499D',
        'method': 'GetParameterValues',
        'datasetname': 'RegionalData',
        'ParameterName': 'KeyCode',
        'ResultFormat': 'json'
    }

    r = requests.get(api_url, params=params)
    res_json = r.json()

    # Get list of available categories
    categories = res_json['BEAAPI']['Results']['ParamValue']

    # Render list of categories
    return render(request, 'regionaldata/index.html', {'category_list': categories})


def select(request, key_code):
    return render(request, 'regionaldata/select.html', {'key_code': key_code})

