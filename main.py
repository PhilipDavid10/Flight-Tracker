from display import show_menu,display_flight_details, display_flights_from_airport
from api import get_flight_by_number, get_flight_by_airport
from parser import extract_flights
from search import find_flight

def main():
    show_menu()
    choice = input("Choice: ")

    if choice == "1":
        find_flight()

    elif choice == "2":
        airport_code = input("\nEnter Airport Code (e.g. LHR): ")
        raw_data = get_flight_by_airport(airport_code)
        flights = extract_flights(raw_data)

        if flights is None:
            print("Unable to find flights")
        else:
            display_flights_from_airport(flights,airport_code)
            find_flight()


    







main()