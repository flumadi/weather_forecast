# Weather_forecast
## Weather Forecast Application with Django  
* Weather Forecast Screenshot Example screenshot of the application*  

## Overview  
A Python-based web application built with Django that provides current weather conditions and a simple 3-day forecast for selected locations.  
The application fetches real-time weather data from the OpenWeatherMap API and presents it in an easy-to-use interface.  

## Features
 -Current Weather Display: Shows temperature, humidity, wind speed, and conditions  
       3-Day Forecast: Simple forecast prediction for upcoming days  
       Multiple Locations: Pre-configured with major world cities  
       Responsive Design: Works on desktop and mobile devices   
       API Integration: Connects with OpenWeatherMap for live data  

## Technology Stack  
   -Backend: Django 4.x    
   -Frontend: HTML5, Bootstrap 5  
   -API: OpenWeatherMap  
   -Database: SQLite (default)  
   
-Dependencies:   
   requests   
   python-dotenv  
   
-Installation Guide  
   Prerequisites    
      -Python 3.7+  
      -pip package manager  
      -OpenWeatherMap API key (free tier available)  
      
## Setup Instructions  
   Clone the repository (or create from the provided code)  
     bash  
        git clone [repository-url]  
        cd weather_forecaster  
        Create and activate virtual environment   
    bash  
        python -m venv venv  
        # Windows  
           venv\Scripts\activate  
        # Mac/Linux  
           source venv/bin/activate  
-Install dependencies  
    bash  
        pip install -r requirements.txt  
        Configure environment variables  
        Create a .env file in the project root:  

## WEATHER_API_KEY=your_openweathermap_api_key  
Apply database migrations  

bash  
python manage.py migrate  
Seed sample locations  

bash  
python manage.py seed_locations  
Create admin user (optional)  

bash  
python manage.py createsuperuser  
Run development server  

bash  
python manage.py runserver  
Access the application  
Open your browser to:  

http://127.0.0.1:8000/  
## Usage Guide   
  -Select a Location  
  -Choose from the dropdown list of available cities  
  -Click "Get Forecast" button  
  -View Weather Information  
Current weather conditions appear at the top  
3-day forecast appears below in card format  
Admin Interface (optional)  
Access /admin to manage locations  
Login with superuser credentials  

## API Configuration  
This application uses the OpenWeatherMap API:  
   -Sign up for a free account at OpenWeatherMap  
   -Get your API key from the account dashboard  
   -Add it to your .env file as WEATHER_API_KEY  
The free tier provides:  
   -60 calls per minute  
   -1,000,000 calls per month  
   -Current weather data only  

## Project Structure  
weather_forecaster/  
├── forecast/  
│   ├── migrations/  
│   ├── __init__.py  
│   ├── admin.py  
│   ├── apps.py  
│   ├── models.py  
│   ├── tests.py  
│   ├── urls.py  
│   ├── views.py  
│   └── templates/  
│       └── forecast/  
│           ├── base.html  
│           ├── index.html  
│           └── forecast.html  
├── weather_forecaster/  
│   ├── __init__.py  
│   ├── asgi.py  
│   ├── settings.py  
│   ├── urls.py  
│   └── wsgi.py  
└── manage.py  

## Customization Options  
Adding New Locations  
 Via Admin Interface  
  -Access /admin  
  -Navigate to Locations section  
  -Add new location with name, latitude, longitude
 Via Management Command   
  -Edit seed_locations.py  
  -Add new locations to the list   
  -Run the command again

## Styling Changes  
Modify the Bootstrap classes in:  
  -forecast/templates/forecast/base.html  
  -forecast/templates/forecast/index.html  
  -forecast/templates/forecast/forecast.html

## Extending Features
 ✅Better Forecasting  
 Implement a proper forecasting API  
 Add more detailed weather data  
 Location Search  
 Add geocoding functionality  
 Implement address lookup  
 User Accounts  
 Enable favorite locations  
 Save search history

## Troubleshooting  
 Common Issues  
  API Not Working  
     -Verify your API key is correct  
     -Check your OpenWeatherMap account status  
     -Ensure you're not exceeding rate limits  

  Template Errors  
    -Verify all template files exist in correct locations  
    -Check for typos in template names/paths

  Database Issues  
    -Run migrations: python manage.py migrate  
    -Create superuser if admin access needed

## License
This project is open-source and available under the MIT License.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests.

## Support
For assistance, please open an issue in the GitHub repository or contact mathiasfridah2@gmail.com.
