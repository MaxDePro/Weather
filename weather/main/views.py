from django.shortcuts import render, redirect

from django.views.generic import View
from django.urls import reverse

from django.core.exceptions import ValidationError

import requests
from .forms import CityForm
from .models import Cities


def add_city(request):
    apikey = 'dc1becbc9e406dc21a63e086658afa7e'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + apikey
    cities = Cities.objects.all()

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        try:
            form.save()
        except ValueError:
            form = CityForm

    form = CityForm()

    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': int(res['main']['temp']),
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)
    context = {'all_info': all_cities, 'form': form}

    return render(request, 'main/weather.html', context)


class DeleteCity(View):
    def get(self, request, name):
        name = Cities.objects.get(name__iexact=name)
        return render(request, 'main/delete_city.html', {'name': name})

    def post(self, request, name):
        name = Cities.objects.get(name__iexact=name)
        name.delete()
        return redirect(reverse('main_page'))
