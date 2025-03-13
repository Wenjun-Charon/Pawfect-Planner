import requests
import pandas as pd
from src.config import YELP_API_KEY

def get_pet_events(location):
    url = "https://api.yelp.com/v3/events"
    headers = {"Authorization": f"Bearer {YELP_API_KEY}"}
    params = {"location": location, "categories": "pets", "limit": 10, "sort_on": "time_start", "sort_by": "desc"}
    response = requests.get(url, headers=headers, params=params)
    events = []

    if response.status_code == 200:
        data = response.json()
        for event in data.get('events', []):
            events.append({
                'Name': event['name'],
                'Date': event.get('time_start', 'Unknown'),
                'Location': event.get('location', {}).get('city', 'Unknown'),
                'URL': event.get('event_site_url', 'N/A')
            })

    return pd.DataFrame(events)
