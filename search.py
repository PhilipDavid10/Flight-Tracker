from api import get_flight_by_number
from display import display_flight_details
from parser import extract_singular_flight

def find_flight():
    flight_number = input("\nEnter Flight Code (e.g. BA123):  ")
    raw_data = get_flight_by_number(flight_number)
    flight = extract_singular_flight(raw_data)
    
    if flight is None:
        print("Unable to find flight")
    else:
        display_flight_details(flight)