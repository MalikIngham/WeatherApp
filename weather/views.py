from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):

    #699497bc3021878c9b2cdd13921dbb4e

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c12a48c9ac1ec37bedd3cc51b1af4e8b'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    cities = City.objects.all()

    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city': city.name,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
        }

        weather_data.append(weather)


    context = {'weather_data' : weather_data, 'form': form}

    return render(request, 'weather/weather.html',context)

