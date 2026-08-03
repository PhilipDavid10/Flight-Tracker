from display import show_menu,display_flight, display_flights_from_airport
from api import get_flight_by_number, get_flight_by_airport

def main():
    show_menu()
    choice = input("Choice: ")

    if choice == "1":
        flight_number = input("\nEnter Flight Code (e.g. BA123):  ")
        flight = get_flight_by_number(flight_number)

        if flight is None:
            print("Unable to find flight")
        else:
            display_flight(flight)

    elif choice == "2":
        airport_code = input("\nEnter Airport Code (e.g. LHR): ")
        flights = get_flight_by_airport(airport_code)

        if flight is None:
            print("Unable to find flights")
        else:
            display_flights_from_airport(flights)


    







main()