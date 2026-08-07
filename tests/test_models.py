from models import Flight

def test_flight_creation():

    flight = Flight(
        number="AA100",
        airline="American Airlines",
        departure="JFK",
        arrival="LHR",
        status="scheduled"
    )

    assert flight.number == "AA100"
    assert flight.airline == "American Airlines"
    assert flight.departure == "JFK"
    assert flight.arrival == "LHR"
    assert flight.status == "scheduled"

def test_flight_to_dict():

    flight = Flight(
            number="AA100",
            airline="American Airlines",
            departure="JFK",
            arrival="LHR",
            status="scheduled"
        )

    result = flight.to_dict()

    assert result["number"] == "AA100"
    assert result["airline"] == "American Airlines"
    assert result["departure"] == "JFK"
    assert result["arrival"] == "LHR"
    assert result["status"] == "scheduled"

def test_flight_missing_optional_data():
    flight = Flight(
            number="AA100",
            airline="American Airlines"
        )

    assert flight.departure is None
    assert flight.arrival is None
    assert flight.latitude is None
    assert flight.longitude is None

def test_flight_to_dict_location_data():
    flight = Flight(
        number="AA100",
        airline="American Airlines",
        latitude=40.5,
        longitude=-70.2,
        altitude=10000,
        speed=500,
        heading=90
    )

    result = flight.to_dict()

    assert result["latitude"] == 40.5
    assert result["longitude"] == -70.2
    assert result["altitude"] == 10000
    assert result["speed"] == 500
    assert result["heading"] == 90