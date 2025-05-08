import requests
import json
import os
from bart_stations import get_address_from_station


API_KEY = '66a2c365f87e536e54d55c6f'
CACHE_PATH = 'cache/place_ids.json'

# Check if the cache exists and load it or make one
if os.path.exists(CACHE_PATH):
    with open(CACHE_PATH, 'r') as f:
        place_ids_cache = json.load(f)
else:
    place_ids_cache = {}

def get_place_id(address):
    """Retrieve Place ID from cache or API."""
    if address in place_ids_cache:
        return place_ids_cache[address]
    else:
        # Call the Google Geocoding API to get the place ID
        url = f'https://cent.ischool-iot.net/api/google/geocode'
        header = { 'X-API-KEY': API_KEY }
        params = { 'location': address }
        response = requests.get(url, headers=header, params=params)
        response.raise_for_status()
        data = response.json()
        if data['status'] == 'OK':
            place_id = data['results'][0]['place_id']
            # Cache the place ID
            place_ids_cache[address] = place_id
            with open(CACHE_PATH, 'w') as f:
                json.dump(place_ids_cache, f)
            return place_id

def get_directions(station_from, station_to, mode="driving"):
    """Retrieve directions between two stations using their names."""
    # Get the addresses for both stations
    address_from = get_address_from_station(station_from)
    address_to = get_address_from_station(station_to)

    # Get the Place IDs for both stations
    place_id_from = get_place_id(address_from)
    place_id_to = get_place_id(address_to)

    if place_id_from and place_id_to:
        # Get directions between the two stations
        url = f'https://cent.ischool-iot.net/api/google/places/directions'
        header = { 'X-API-KEY': API_KEY }
        params = {
            'mode': mode,
            'destination_place_id': place_id_to,
            'origin_place_id': place_id_from
        }
        response = requests.get(url = url, headers=header, params=params)
        response.raise_for_status()
        data = response.json()

        if data['status'] == 'OK':
            duration = data['routes'][0]['legs'][0]['duration']['text']
            return duration
        else:
            print("Error fetching directions:", data['status'])
            return None
    else:
        return "Error: Could not retrieve Place IDs for one or both stations."
    