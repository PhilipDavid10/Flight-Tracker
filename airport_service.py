from api import get_airports
from parser import extract_airport

def get_flight_airports(flight):
    dep_data = get_airports(flight.departure)
    dep_airport = extract_airport(dep_data)

    arr_data = get_airports(flight.arrival)
    arr_airport = extract_airport(arr_data)

    return dep_airport, arr_airport