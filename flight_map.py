import webbrowser
import folium
from parser import extract_airport
from api import get_airports

def open_map(trackekd_flights):

    m = folium.Map(location=[0,0], zoom_start=2)

    for flight in trackekd_flights:

        if flight.longitude is None or flight.latitude is None:
            continue

        folium.Marker(location=[flight.latitude,flight.longitude],
                    tooltip=f"{flight.number}",
                    popup=f"Flight Code: {flight.number}",
                    icon=folium.Icon(color='blue', prefix='fa', icon='plane')
                    ).add_to(m)

        dep_data = get_airports(flight.departure)
        dep_airport = extract_airport(dep_data)

        arr_data = get_airports(flight.arrival)
        arr_airport = extract_airport(arr_data)

        draw_flight_path(m, dep_airport, arr_airport, flight)

        m.save("flight_map.html")

        webbrowser.open("flight_map.html")

def draw_flight_path(m, dep_airport, arr_aiport, flight):
    coordinates = [
        [dep_airport["latitude"],dep_airport["longitude"]],
        [flight.latitude,flight.longitude],
        [arr_aiport["latitude"],arr_aiport["longitude"]]
        ]

    folium.PolyLine(
        coordinates,
        weight=3,
        tooltip=f"{flight.number} flight path"
    ).add_to(m)