import requests
import json
from config import API_KEY, FLIGHT_URL, MULTIPLE_FLIGHTS_URL, AIRPORTS_URL
from models import Flight


def get_flight_by_number(flight_number):
    params={
        "flight_iata": flight_number,
        "api_key": API_KEY
    }
    try:
        response = requests.get(
            FLIGHT_URL,
            params=params
        )
        
        data = response.json()

        if "error" in data:
            return None
        
        return data

    except requests.RequestException:
        return None


def get_flight_by_airport(airport_code):
    params = {
        "dep_iata": airport_code,
        "api_key": API_KEY
    }
    try:
        response = requests.get(
            MULTIPLE_FLIGHTS_URL,
            params=params
        )

        data = response.json()

        if "error" in data:
            return None
        
        return data

    except requests.RequestException:
        return None
    
def get_airports(airport_code):
    params={
        "iata_code": airport_code,
        "api_key": API_KEY
    }

    try:
        response = requests.get(
            AIRPORTS_URL,
            params=params
        )

        data = response.json()

        if "error" in data:
            return None
        
        return data

    except requests.RequestException:
        return None