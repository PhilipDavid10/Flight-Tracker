from display import display_flight_details, display_map_menu
from data.history import save_history
from flight_map import open_map

def handle_flight(flight, tracked_flights):
    if flight is None:
        return tracked_flights

    display_flight_details(flight)
    save_history(flight)

    tracked_flights = [f for f in tracked_flights
                            if f.number != flight.number]
    tracked_flights.append(flight)

    map_choice = display_map_menu()

    if map_choice == "1":
        open_map(tracked_flights)

    return tracked_flights