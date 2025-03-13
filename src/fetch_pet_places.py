import requests
import pandas as pd
from src.config import GOOGLE_PLACES_API_KEY, YELP_API_KEY

def get_lat_lon_from_location(location):
    geo_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {'address': location, 'key': GOOGLE_PLACES_API_KEY}
    response = requests.get(geo_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data.get('results'):
            return data['results'][0]['geometry']['location']
    return None

def get_pet_friendly_places(location, radius=5000):
    lat_lon = get_lat_lon_from_location(location)
    if not lat_lon:
        return pd.DataFrame()

    categories = ['dog park', 'pet store', 'pet grooming', 'veterinary clinic', 'pet-friendly café', 'pet-friendly hotel']
    places = []

    for keyword in categories:
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params = {'location': f"{lat_lon['lat']},{lat_lon['lng']}", 'radius': radius, 'keyword': keyword, 'key': GOOGLE_PLACES_API_KEY}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            for place in data.get('results', []):
                places.append({
                    'Name': place['name'],
                    'Address': place.get('vicinity', 'N/A'),
                    'Rating': place.get('rating', 0),
                    'Category': keyword,
                    'Source': 'Google'
                })

    return pd.DataFrame(places)
