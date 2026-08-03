import requests
import json
from config import API_KEY, FLIGHT_URL, AIRPORT_URL
from models import Flight


def get_flight_by_number(flight_number):
    params={
        "flight_iata": flight_number,
        "api_key": API_KEY
    }

    response = requests.get(
        FLIGHT_URL,
        params=params
    )

    data = response.json()

    if "error" in data:
        return None

    flight = data["response"]


    return Flight(
        number=flight["flight_iata"],
        airline=flight["airline_iata"],
        departure=flight["dep_iata"],
        arrival=flight["arr_iata"],
        status=flight["status"])


def get_flight_by_airport(airport_code):
    params = {
        "dep_iata": airport_code,
        "api_key": API_KEY
    }

    response = requests.get(
        AIRPORT_URL,
        params=params
    )

    data = response.json()

    if "error" in data:
        return None
    else:
        return data
    
    