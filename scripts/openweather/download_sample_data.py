#!/usr/bin/env python3

import json
import os
from base import get_weather_from_api

# fmt: off
cities = [ "Amsterdam", "Athens", "Atlanta", "Auckland", "Austin", "Baghdad", "Baltimore", "Bangkok", "Barcelona", "Beijing", "Berlin", "Birmingham", "Bogota", "Boston", "Brussels", "Bucharest", "Budapest", "Buenos Aires", "Cairo", "Calgary", "Cape Town", "Caracas", "Charlotte", "Chennai", "Chicago", "Copenhagen", "Dallas", "Delhi", "Denver", "Detroit", "Dubai", "Dublin", "Dusseldorf", "Frankfurt", "Geneva", "Guangzhou", "Hamburg", "Hanoi", "Helsinki", "Ho Chi Minh City", "Hong Kong", "Houston", "Istanbul", "Jakarta", "Johannesburg", "Kiev", "Kuala Lumpur", "Las Vegas", "Lima", "Lisbon", "London", "Los Angeles", "Madrid", "Manila", "Melbourne", "Mexico City", "Miami", "Milan", "Minneapolis", "Montreal", "Moscow", "Mumbai", "Munich", "Nairobi", "Nashville", "New Orleans", "New York City", "Oslo", "Paris", "Philadelphia", "Phoenix", "Prague", "Riyadh", "Rome", "Saint Petersburg", "San Francisco", "Santiago", "Sao Paulo", "Seattle", "Seoul", "Shanghai", "Shenzhen", "Singapore", "Stockholm", "Sydney", "Taipei", "Tehran", "Tel Aviv", "Tokyo", "Toronto", "Vancouver", "Vienna", "Warsaw", "Washington, D.C.", "Zurich" ]
# fmt: on


for api in ["weather", "forecast", "air_pollution"]:
    os.makedirs(f"data/2023-09-09/{api}", exist_ok=True)

    for city in cities:
        filename = f"data/2023-09-09/{api}/{city}.json"

        if os.path.exists(filename):
            continue

        r = get_weather_from_api(city, api, save_to_file=False)

        with open(filename, "w") as f:
            json.dump(r, f, indent=4)

        print(f"Saved {api} for {city}")
