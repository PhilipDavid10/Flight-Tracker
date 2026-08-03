def show_menu():
    print("\n========================")
    print("     Flight Tracker     ")
    print("========================\n")

    menu_options = ["Search by Flight Number", "Search by Airport", "View Search History", "Exit"]

    for number, options in enumerate(menu_options, start=1):
        print(f"{number}. {options}")

    print("")

def display_flight(flight):
    print("\n========================")
    print("   Flight Information   ")
    print("========================\n")

    print(f"Flight: {flight.number}")
    print(f"Airline: {flight.airline}")
    print(f"Departure Airport: {flight.departure}")
    print(f"Arrival Airport: {flight.arrival}")
    print(f"Status: {flight.status}")

def display_flights_from_airport(flights, airport_code):
    print("\n========================")
    print(f"   Flights from {airport_code}")
    print("========================\n")

    for flight in flights:
        print(f"Flight: {flight.number}")
        print(f"Airline: {flight.airline}")
        print(f"Status: {flight.status}")
        print("----------------")

        