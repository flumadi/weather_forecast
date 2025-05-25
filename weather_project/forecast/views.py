import os
import requests
import datetime
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Location, WeatherData
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

if not WEATHER_API_KEY:
    raise ValueError("Missing WEATHER_API_KEY in environment variables")

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
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def index(request):
    locations = Location.objects.all().order_by('name')
    popular_cities = Location.objects.filter(
        name__in=['New York', 'London', 'Tokyo', 'Paris', 'Sydney']
    )[:6]
    
    context = {
        'locations': locations,
        'popular_cities': popular_cities,
    }
    return render(request, 'forecast/index.html', context)

def forecast(request):
    if request.method == 'POST':
        location_id = request.POST.get('location')
        try:
            location = Location.objects.get(id=location_id)
            weather_data = get_weather_data(location)
            
            if weather_data:
                current = weather_data['current']
                daily = weather_data['daily'][:3]  # Get 3-day forecast
                
                # Save weather data to database
                WeatherData.objects.create(
                    location=location,
                    temperature=current['temp'],
                    humidity=current['humidity'],
                    wind_speed=current['wind_speed'],
                    description=current['weather'][0]['description'],
                    icon=current['weather'][0]['icon']
                )
                
                context = {
                    'location': location,
                    'current': {
                        'temp': current['temp'],
                        'humidity': current['humidity'],
                        'wind_speed': current['wind_speed'],
                        'description': current['weather'][0]['description'],
                        'icon': current['weather'][0]['icon'],
                        'temp_max': current.get('temp_max', current['temp']),
                        'temp_min': current.get('temp_min', current['temp']),
                        'pressure': current.get('pressure', 0),
                        'feels_like': current.get('feels_like', current['temp']),
                        'visibility': current.get('visibility', 0),
                        'uvi': current.get('uvi', 0),
                        'time': datetime.datetime.fromtimestamp(current['dt']),
                    },
                    'forecast': [
                        {
                            'date': datetime.datetime.fromtimestamp(day['dt']),
                            'temp_day': day['temp']['day'],
                            'temp_night': day['temp']['night'],
                            'temp_eve': day['temp']['eve'],
                            'temp_morn': day['temp']['morn'],
                            'humidity': day['humidity'],
                            'wind_speed': day['wind_speed'],
                            'pressure': day['pressure'],
                            'description': day['weather'][0]['description'],
                            'icon': day['weather'][0]['icon'],
                            'pop': day.get('pop', 0) * 100,  # Probability of precipitation
                            'uvi': day.get('uvi', 0),
                        } for day in daily
                    ],
                    'hourly': weather_data.get('hourly', [])[:12],
                }
                return render(request, 'forecast/forecast.html', context)
        
        except Location.DoesNotExist:
            return redirect('index')
        except Exception as e:
            print(f"Error processing forecast: {e}")
            return redirect('index')
    
    return render(request, 'forecast/forecast.html')

def recent_searches(request):
    if request.user.is_authenticated:
        recent = WeatherData.objects.filter(
            location__in=request.user.profile.favorite_locations.all()
        ).order_by('-timestamp')[:5]
    else:
        recent = WeatherData.objects.all().order_by('-timestamp')[:5]
    
    context = {'recent_searches': recent}
    return render(request, 'forecast/recent.html', context)