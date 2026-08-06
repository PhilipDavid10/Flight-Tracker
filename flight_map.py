import webbrowser
import folium


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

        m.save("flight_map.html")

        webbrowser.open("flight_map.html")
