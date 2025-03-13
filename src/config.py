import requests_cache
import os

# Initialize caching to store API responses for 1 hour
requests_cache.install_cache('pawfect_cache', expire_after=3600)

# API Keys (Load from environment variables)
GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY", "your_google_api_key")
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY", "your_openweathermap_api_key")
YELP_API_KEY = os.getenv("YELP_API_KEY", "your_yelp_api_key")
