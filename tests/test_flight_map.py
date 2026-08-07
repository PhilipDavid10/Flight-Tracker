from flight_map import open_map, create_path_coordinates
from models import Flight

def test_map_ignores_missing_coordinates(tmp_path):

    flights = [
        Flight(
        number="AA100",
        airline="American Airlines",
        latitude=None,
        longitude=None
    )]

    open_map(flights, tmp_path / "flight_map.html")

    assert (tmp_path / "flight_map.html").exists()

def test_map_creation(tmp_path):
    flights = [
        Flight(
            number="AA100",
            airline="American Airlines",
            latitude=40.0,
            longitude=-70
        )
    ]

    map_file = tmp_path / "flight_map.html"

    open_map(flights, map_file)

    assert map_file.exists()

def test_flight_path_coordinates():
    flight = Flight(
        number="AA100",
        airline="American Airlines",
        latitude=30,
        longitude=-50
    )

    dep_airport = {
        "latitude": 40,
        "longitude": -70
    }

    arr_airport = {
        "latitude": 50,
        "longitude": -10
    }

    coordinates=create_path_coordinates(dep_airport,arr_airport,flight)

    assert coordinates == [
        [40,-70],
        [30,-50],
        [50,-10]
    ]