import webbrowser
import folium


def open_map(flight):
    m = folium.map(location=(flight.longitude,flight.latitude))
    print(m)