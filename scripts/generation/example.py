#!/usr/bin/env python3

import requests
import sys
import argparse
import os

sys.path.append("scripts/openweather/")

from base import get_weather_from_json

# get node number from command line
parser = argparse.ArgumentParser()
parser.add_argument("node", help="Node number (see the instructions for details)", type=int)
args = parser.parse_args()


if __name__ == "__main__":
    # the node on the cluster to use
    NODE = args.node
    API_URL = f"http://quest.ms.mff.cuni.cz/nlg/practicald2t-node{NODE}/generate"
    API_KEY = os.environ.get("UFAL_LLM_API_KEY")

    data = get_weather_from_json("data/2023-09-09/weather/Prague.json")

    prompt = f"Your task is to write a one-paragraph weather forecast for Prague as of today. The output should include all relevant information such as temperature, humidity, wind speed and direction, visibility, cloud cover, sunrise/sunset times, etc., in a clear and concise manner. Please use appropriate units throughout your response.\n{data}\n"

    args = {
        "api_key": API_KEY,
        "prompt": prompt,
        "max_length": 512,
        "temperature": 0.9,
        "repetition_penalty": 1.2,
        "do_sample": False,
        # "top_p": 0.95,
        # "top_k": 50,
    }
    response = requests.post(
        API_URL,
        json=args,
    )
    j = response.json()

    try:
        print(j["out"]["choices"][0]["text"])
    except KeyError:
        print(j)

    """
    Example output from llama-2-7b-chat-hf (fp16):
    --------------------------------------------------

    Here's the forecasted data:
    As of today (March 2nd), Prague will experience mostly clear skies with a high temperature of around 28°C (82°F) during the day and a low of about 27.7°C (81.9°F) at night. Humidity levels are expected to be moderate at 40%. Wind speeds will range from 4-6 mph (6-9 km/h) coming from the northwest, gusting up to 4.02 mph (6.4 km/h). Visibility will be excellent at 10,000 meters (32,808 feet). There will be no clouds present in the area. Sunrise today was at 6:37 AM, while sunset will occur at 7:36 PM.
    """
