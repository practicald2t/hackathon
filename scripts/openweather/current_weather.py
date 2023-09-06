#!/usr/bin/env python3

import argparse

from base import lookup_weather


def pretty_print(data):
    # Extract relevant data from the response
    coordinates = data["coord"]
    weather_info = data["weather"][0]
    main_info = data["main"]
    visibility = data["visibility"]
    wind_info = data["wind"]
    rain_info = data.get("rain", {"1h": 0})
    clouds_info = data["clouds"]
    sys_info = data["sys"]

    # Print the current weather forecast
    print("Current Weather for", data["name"])
    print("-" * 36)
    print(f"Weather:       {weather_info['main']} - {weather_info['description']}")
    print(f"Temperature:   {main_info['temp']:.2f}°C")
    print(f"Feels Like:    {main_info['feels_like']:.2f}°C")
    print(f"Temp Min/Max:  {main_info['temp_min']:.2f}°C / {main_info['temp_max']:.2f}°C")
    print(f"Pressure:      {main_info['pressure']} hPa")
    print(f"Humidity:      {main_info['humidity']}%")
    print(f"Visibility:    {visibility} meters")
    print(f"Wind:          {wind_info['speed']:.2f} m/s")
    print(f"Rain (1h):     {rain_info['1h']:.2f} mm")
    print(f"Cloudiness:    {clouds_info['all']}%")
    print(f"Sunrise:       {sys_info['sunrise']} (Unix Timestamp)")
    print(f"Sunset:        {sys_info['sunset']} (Unix Timestamp)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and display current weather data")
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-l", "--location", type=str, help="Fetch weather from OpenWeather for a location")
    group.add_argument("-j", "--json", type=str, help="Load the OpenWeather data from an existing JSON file")

    args = parser.parse_args()
    if not (args.location or args.json):
        parser.error("Specify either location or path to a JSON file.")

    data = lookup_weather(location=args.location, json=args.json, api="weather")

    pretty_print(data)
