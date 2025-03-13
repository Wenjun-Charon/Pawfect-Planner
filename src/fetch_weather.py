import requests
from src.config import OPENWEATHERMAP_API_KEY
def get_weather(location):
    url = "http://api.openweathermap.org/data/2.5/weather"
    if location.isdigit():
        params = {'zip': f"{location},US", 'appid': OPENWEATHERMAP_API_KEY, 'units': 'metric'}
    else:
        params = {'q': location, 'appid': OPENWEATHERMAP_API_KEY, 'units': 'metric'}
        
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            'City': data.get('name', 'Unknown'),
            'Temperature': data['main']['temp'],
            'Weather': data['weather'][0]['description'].capitalize(),
            'Wind Speed': data['wind']['speed'],
            'Recommendation': get_weather_recommendation(data['main']['temp'], data['weather'][0]['description'])
        }
    return {}
