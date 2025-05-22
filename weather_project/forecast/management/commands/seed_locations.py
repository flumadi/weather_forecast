from django.core.management.base import BaseCommand
from forecast.models import Location

class Command(BaseCommand):
    help = 'Seeds the database with initial locations'
    
    def handle(self, *args, **options):
        locations = [
            {'name': 'New York', 'latitude': 40.7128, 'longitude': -74.0060, 'country_code': 'US'},
            {'name': 'London', 'latitude': 51.5074, 'longitude': -0.1278, 'country_code': 'GB'},
            {'name': 'Tokyo', 'latitude': 35.6762, 'longitude': 139.6503, 'country_code': 'JP'},
            {'name': 'Sydney', 'latitude': -33.8688, 'longitude': 151.2093, 'country_code': 'AU'},
            {'name': 'Cape Town', 'latitude': -33.9249, 'longitude': 18.4241, 'country_code': 'ZA'},
        ]
        
        for loc_data in locations:
            Location.objects.get_or_create(**loc_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded locations'))