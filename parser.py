def extract_flights(data):
    flights = data["response"]

    cleaned_flights = []

    for flight in flights:
        cleaned_flights.append({
            "Flight Number": flight.get("flight_iata"),
            "Airline": flight.get("airline_iata"),
            "Arrival": flight.get("arr_iata"),
            "Status": flight.get("status")
        })