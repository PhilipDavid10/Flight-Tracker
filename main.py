from display import show_menu, display_flights_from_airport, display_flight_details, display_history, display_map_menu
from api import get_flight_by_airport
from parser import extract_flights
from search import find_flight
from data.history import save_history, load_history
from flight_map import open_map


def main():
    tracked_flights = []

    while True:
        show_menu()
        choice = input("Choice: ")

        if choice == "1":
            flight_number = input("\nEnter Flight Code (e.g. BA123):  ")
            flight = find_flight(flight_number)

            if flight:
                display_flight_details(flight)
                save_history(flight)

                tracked_flights = [f for f in tracked_flights
                                       if f.number != flight.number]
                tracked_flights.append(flight)

            choice = display_map_menu()

            if choice == "1":
                open_map(tracked_flights)
            


        elif choice == "2":
            airport_code = input("\nEnter Airport Code (e.g. LHR): ")
            raw_data = get_flight_by_airport(airport_code)
            flights = extract_flights(raw_data)

            if flights is None:
                print("Unable to find flights")
            else:
                display_flights_from_airport(flights,airport_code)
                flight_number = input("\nEnter Flight Code (e.g. BA123):  ")
                flight = find_flight(flight_number)

            if flight:
                display_flight_details(flight)
                save_history(flight)

                tracked_flights = [f for f in tracked_flights
                                                       if f.number != flight.number]
                tracked_flights.append(flight)
                
                choice = display_map_menu()
                
                if choice == "1":
                    open_map(tracked_flights)
            
            
        elif choice == "3":
            history = load_history()
            display_history(history)

        elif choice == "4":
            break


    







main()