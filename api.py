import requests
import json
from config import API_KEY, BASE_URL

def search_flight(flight_number):
    params={
        "flight_iata": flight_number,
        "api_key": API_KEY
    }

    response = requests.get(
        BASE_URL,
        params=params
    )

    return response.json()
    