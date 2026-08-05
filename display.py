def show_menu():
    print("\n========================")
    print("     Flight Tracker     ")
    print("========================\n")

    menu_options = ["Search by Flight Number", "Search by Airport", "View Search History", "Exit"]

    for number, options in enumerate(menu_options, start=1):
        print(f"{number}. {options}")

    print("")

def display_flight_details(flight):
    print("\nFlight Information")
    print("-"*20)

    print(f"Flight: {flight.number}")
    print(f"Airline: {flight.airline}")
    print(f"Route: {flight.departure} -> {flight.arrival}")
    print(f"Status: {flight.status}")

    print("\nLive Data")
    print("-"*20)

    print(f"Altitude: {flight.altitude} m")
    print(f"Speed: {flight.speed} km/h")
    print(f"Heading: {flight.heading}")
    print(f"Longitude: {flight.longitude}")
    print(f"Latitude: {flight.latitude}")

    print("\nTimes")
    print("-"*20)

    print(f"Departure Time: {flight.dep_time} UTC")
    print(f"Arrival Time: {flight.arr_time} UTC")
    

def display_flights_from_airport(flights, airport_code):
    print(f"Flights from {airport_code}")
    print("-"*10)

    print(f"{'Flight':<10} | {'Airline':<15} | {'Route':<15} | {'Status':<12}")
    print(f"-"*65)

    for flight in flights:
        print(flight)

def display_history(history):
    print("\nPrevious Search History")
    print("-"*30)
    print("")

    print(f"{'Flight':<10} | {'Airline':<20} | {'Route':<15} | {'Status':<12}")
    print(f"-"*65)

    for flight in history:
        departure = flight.get("departure") or "unknown"
        arrival = flight.get("arrival") or "unknown"
        route = f"{departure} -> {arrival}"

        print(
            f"{flight.get('number') or 'unknown':<10} | "
            f"{flight.get('airline') or 'unknown':<20} | "
            f"{route:<15} | "
            f"{flight.get('status') or 'unknown':<12}"
        )