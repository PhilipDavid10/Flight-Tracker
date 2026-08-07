from parser import extract_singular_flight

def test_extract_singular_flight():

    data = {
        "response": {
            "flight_iata": "AA100",
            "airline_name": "American Airlines",
            "dep_iata": "JFK",
            "arr_iata": "LHR",
            "status": "scheduled",
            "lat": 40.0,
            "lng": -70.0,
            "alt": 10000,
            "speed": 500,
            "dir": 90
        }
    }

    flight = extract_singular_flight(data)

    assert flight.number == "AA100"
    assert flight.airline == "American Airlines"
    assert flight.departure == "JFK"
    assert flight.arrival == "LHR"
    assert flight.status == "scheduled"

def test_extract_flight_missing_data():
    data = {
            "response": {
                "flight_iata": "AA100",
                "airline_name": None,
                "dep_iata": "JFK",
                "arr_iata": "LHR",
                "status": None,
                "lat": 40.0,
                "lng": None,
                "alt": 10000,
                "speed": 500,
                "dir": None
            }
        }

    flight = extract_singular_flight(data)

    assert flight.airline is None
    assert flight.status is None
    assert flight.longitude is None
    assert flight.heading is None

def test_extract_flight_not_found():

    data = {
        "error": {
            "message": "Flight not found"
        }
    }

    result = extract_singular_flight(data)

    assert result is None