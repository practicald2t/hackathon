#!/usr/bin/env python3

import requests
import argparse
from geopy.geocoders import Nominatim

# OpenWeather API URL
base_url = "https://api.openweathermap.org/data/2.5/forecast"

# API Key (replace with your own API key)
api_key = "2120c2474fb0b26d4b7122dfe9cfbf1b"

# Define the argument parser
parser = argparse.ArgumentParser(description="Fetch and display weather forecast data")
parser.add_argument("-l", "--location", type=str, required=True, help="Location for weather forecast")

# Parse command line arguments
args = parser.parse_args()

# Use Nominatim to get latitude and longitude from the location
geolocator = Nominatim(user_agent="weather_app")
location = geolocator.geocode(args.location)
if location:
    lat, lon = location.latitude, location.longitude
else:
    print("Location not found. Please check the input.")
    exit()

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
    data = response.json()

    # Extract relevant data from the response
    forecasts = data["list"]

    # Create ASCII charts
    print("Weather Forecast for", args.location)
    print("Date and Time       Temperature (°C)   Pressure (hPa)   Humidity (%)   Weather Description")
    print("-" * 92)
    for forecast in forecasts:
        dt_txt = forecast["dt_txt"]
        temperature = forecast["main"]["temp"]
        pressure = forecast["main"]["pressure"]
        humidity = forecast["main"]["humidity"]
        weather_desc = forecast["weather"][0]["description"]

        # Create an ASCII chart for temperature, pressure, humidity
        temp_chart = "#" * int(temperature)
        pressure_chart = "#" * int(pressure / 10)  # Normalize pressure for the chart
        humidity_chart = "#" * int(humidity)

        # Print the forecast data with ASCII charts
        print(f"{dt_txt:<20}   {temperature:<16.2f}   {pressure:<14.2f}   {humidity:<12}   {weather_desc}")

else:
    print("Error fetching weather data. Status code:", response.status_code)
