from models import Flight

def extract_singular_flight(data):
    if data is None:
        return None

    flight = data.get("response")

    if flight is None:
        return None
    
    return Flight(
                    number=flight.get("flight_iata"),
                    airline=flight.get("airline_name"),
                    departure=flight.get("dep_iata"),
                    arrival=flight.get("arr_iata"),
                    status=flight.get("status"),
                    aircraft=flight.get("model"),
                    altitude=flight.get("alt"),
                    speed=flight.get("speed"),
                    heading=flight.get("dir"),
                    longitude=flight.get("lng"),
                    latitude=flight.get("lat"),
                    dep_time=flight.get("dep_time_utc"),
                    arr_time=flight.get("arr_time_utc")
                )

def extract_flights(data):
    flights = data["response"]

    cleaned_flights = []

    for flight in flights:
        cleaned_flights.append(
            Flight(
                number=flight.get("flight_iata"),
                airline=flight.get("airline_iata"),
                departure=flight.get("dep_iata"),
                arrival=flight.get("arr_iata"),
                status=flight.get("status"),
                aircraft=flight.get("model"),
                altitude=flight.get("alt"),
                speed=flight.get("speed"),
                heading=flight.get("dir"),
                longitude=flight.get("lng"),
                latitude=flight.get("lat"),
                dep_time=flight.get("dep_time_utc"),
                arr_time=flight.get("arr_time_utc")
            ))

    return cleaned_flights

def extract_airport(data):
    airport = data["response"][0]

    return {
        "code": airport["iata_code"],
        "longitude": airport["lng"],
        "latitude": airport["lat"]
    }
    