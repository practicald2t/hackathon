#!/usr/bin/env python3

import requests
import argparse
from geopy.geocoders import Nominatim
import os
import json
import datetime


def get_coordinates(location):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(location)
    if location:
        lat, lon = location.latitude, location.longitude
    else:
        raise ValueError("Location not found. Please check the input.")

    return lat, lon


def get_weather_from_api(location, api, save_to_file=True):
    # OpenWeather API URL
    base_url = f"https://api.openweathermap.org/data/2.5/{api}"
    api_key = os.environ.get("OPENWEATHER_API_KEY")

    # Use Nominatim to get latitude and longitude from the location

    lat, lon = get_coordinates(location)

    # Construct the API request URL
    params = {
        "lat": lat,
        "lon": lon,
        "units": "metric",
        "mode": "json",
        "appid": api_key,
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        j = response.json()

        if save_to_file:
            # Save the response as JSON
            os.makedirs(f"data/fetched/{api}", exist_ok=True)
            current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            with open(f"data/fetched/{api}/{current_time}_{lat:.2f},{lon:.2f}.json", "w") as f:
                json.dump(j, f, indent=4)

        return j
    else:
        print("Error fetching weather data. Status code:", response.status_code)


def get_weather_from_json(json_file):
    with open(json_file) as f:
        return json.load(f)


def lookup_weather(location, json, api="weather"):
    if location:
        data = get_weather_from_api(location, api=api)
    elif json:
        data = get_weather_from_json(json)

    return data
