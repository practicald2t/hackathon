#!/usr/bin/env python3

import argparse

from base import lookup_weather


def pretty_print(data):
    # Extract relevant data from the response
    forecasts = data["list"]

    # Create ASCII charts
    print("Weather Forecast for", data["city"].get("name", "Unknown"))
    print("Date and Time         Temp (°C)   Wind Speed (m/s)   Humidity (%)   Description")
    print("-" * 92)
    for forecast in forecasts:
        dt_txt = forecast["dt_txt"]
        temperature = forecast["main"]["temp"]
        wind_speed = forecast["wind"]["speed"]
        humidity = forecast["main"]["humidity"]
        weather_desc = forecast["weather"][0]["description"]

        # Print the forecast data with ASCII charts
        print(f"{dt_txt:<21}   {temperature:<13.2f}   {wind_speed:<14.2f}   {humidity:<9}   {weather_desc}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and display weather forecast data")
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-l", "--location", type=str, help="Fetch weather from OpenWeather for a location")
    group.add_argument("-j", "--json", type=str, help="Load the OpenWeather data from an existing JSON file")

    args = parser.parse_args()
    if not (args.location or args.json):
        parser.error("Specify either location or path to a JSON file.")

    data = lookup_weather(location=args.location, json=args.json, api="forecast")

    pretty_print(data)
