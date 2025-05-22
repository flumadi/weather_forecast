import os
import requests
from django.shortcuts import render
from django.conf import settings
from .models import Location, WeatherData
from dotenv import load_dotenv

load_dotenv()

def get_weather_data(location):
    api_key = os.getenv('WEATHER_API_KEY')
    base_url = "https://api.openweathermap.org/data/2.5/onecall"
    
    params = {
        'lat': location.latitude,
        'lon': location.longitude,
        'exclude': 'minutely,hourly',
        'appid': api_key,
        'units': 'metric'
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def index(request):
    locations = Location.objects.all()
    context = {'locations': locations}
    return render(request, 'forecast/index.html', context)

def forecast(request):
    if request.method == 'POST':
        location_id = request.POST.get('location')
        location = Location.objects.get(id=location_id)
        
        weather_data = get_weather_data(location)
        
        if weather_data:
            current = weather_data['current']
            daily = weather_data['daily'][:3]  # Get 3-day forecast
            
            context = {
                'location': location,
                'current': {
                    'temp': current['temp'],
                    'humidity': current['humidity'],
                    'wind_speed': current['wind_speed'],
                    'description': current['weather'][0]['description'],
                    'icon': current['weather'][0]['icon'],
                },
                'forecast': [
                    {
                        'date': day['dt'],
                        'temp_day': day['temp']['day'],
                        'temp_night': day['temp']['night'],
                        'humidity': day['humidity'],
                        'wind_speed': day['wind_speed'],
                        'description': day['weather'][0]['description'],
                        'icon': day['weather'][0]['icon'],
                    } for day in daily
                ]
            }
            
            return render(request, 'forecast/forecast.html', context)
    
    return render(request, 'forecast/forecast.html')