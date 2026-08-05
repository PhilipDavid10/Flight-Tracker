from api import get_flight_by_number
from parser import extract_singular_flight

def find_flight(flight_number):
    raw_data = get_flight_by_number(flight_number)
    flight = extract_singular_flight(raw_data)

    if flight is None:
        print("Flight not found")
        return
    
    return flight