import webbrowser
import folium
from airport_service import get_flight_airports

def create_map():
    m = folium.Map(location=[0,0], zoom_start=2)
    return m

def add_flight_marker(m, flight):
    if flight.latitude is None or flight.longitude is None:
        return

    folium.Marker(location=[flight.latitude,flight.longitude],
                        tooltip=f"{flight.number}",
                        popup=f"Flight Code: {flight.number}",
                        icon=folium.Icon(color='blue', prefix='fa', icon='plane')
                        ).add_to(m)

def draw_flight_path(m, dep_airport, arr_aiport, flight):
    if (
        flight.latitude is None
        or flight.longitude is None
        or dep_airport["latitude"] is None
        or dep_airport["longitude"] is None
        or arr_aiport["latitude"] is None
        or arr_aiport["longitude"] is None
    ):
        return


    coordinates = create_path_coordinates(dep_airport,arr_aiport,flight)

    folium.PolyLine(
        coordinates,
        weight=3,
        tooltip=f"{flight.number} flight path"
    ).add_to(m)


def open_map(tracked_flights,filename="flight_map.html"):

    m = create_map()

    for flight in tracked_flights:
        if flight.latitude is None or flight.longitude is None:
            continue
               
        dep_airport, arr_airport = get_flight_airports(flight)

        if dep_airport is None or arr_airport is None:
            continue
        
        add_flight_marker(m, flight)
        draw_flight_path(m, dep_airport, arr_airport, flight)

    m.save(filename)
    webbrowser.open(filename)

def create_path_coordinates(dep_airport, arr_airport, flight):
    return [
        [
            dep_airport["latitude"],
            dep_airport["longitude"]
        ],
        [
            flight.latitude,
            flight.longitude
        ],
        [
            arr_airport["latitude"],
            arr_airport["longitude"]
        ]
    ]