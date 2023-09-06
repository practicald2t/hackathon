#!/usr/bin/env python3

import argparse

from base import lookup_weather


def pretty_print(data):
    # Extract relevant data from the response
    coordinates = data["coord"]
    pollution_info = data["list"][0]
    main_info = pollution_info["main"]
    components_info = pollution_info["components"]

    # Print the air pollution data
    print(f"Air Pollution Data for {coordinates['lat']:.2f}, {coordinates['lon']:.2f}")
    print("-" * 36)
    print("Air Quality Index (AQI):", main_info["aqi"])
    print("Air Quality Index Description:")
    print("1 = Good")
    print("2 = Fair")
    print("3 = Moderate")
    print("4 = Poor")
    print("5 = Very Poor")
    print("Concentration of CO (Carbon monoxide): {} μg/m³".format(components_info["co"]))
    print("Concentration of NO (Nitrogen monoxide): {} μg/m³".format(components_info["no"]))
    print("Concentration of NO2 (Nitrogen dioxide): {} μg/m³".format(components_info["no2"]))
    print("Concentration of O3 (Ozone): {} μg/m³".format(components_info["o3"]))
    print("Concentration of SO2 (Sulphur dioxide): {} μg/m³".format(components_info["so2"]))
    print("Concentration of PM2.5 (Fine particles matter): {} μg/m³".format(components_info["pm2_5"]))
    print("Concentration of PM10 (Coarse particulate matter): {} μg/m³".format(components_info["pm10"]))
    print("Concentration of NH3 (Ammonia): {} μg/m³".format(components_info["nh3"]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and display current weather data")
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-l", "--location", type=str, help="Fetch weather from OpenWeather for a location")
    group.add_argument("-j", "--json", type=str, help="Load the OpenWeather data from an existing JSON file")

    args = parser.parse_args()
    if not (args.location or args.json):
        parser.error("Specify either location or path to a JSON file.")

    data = lookup_weather(location=args.location, json=args.json, api="air_pollution")

    pretty_print(data)
