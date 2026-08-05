class Flight():
    def __init__(self, number, airline, departure=None, arrival=None, status=None, aircraft=None, altitude=None, speed=None, heading=None,longitude=None,latitude=None,dep_time=None,arr_time=None):
        self.number = number
        self.airline = airline
        self.departure = departure
        self.arrival = arrival
        self.status = status
        self.aircraft = aircraft 
        self.altitude = altitude
        self.speed = speed
        self.heading = heading
        self.longitude= longitude
        self.latitude = latitude
        self.dep_time = dep_time
        self.arr_time = arr_time

    def __str__(self):
        route = f"{self.departure or 'unknown'} -> {self.arrival or 'unknown'}"
        return(
            f"{self.number or 'unknown':<10} | {self.airline or 'unknown':<15} | "
            f"{route or 'unknown':<15} | {self.status or 'unknown':<12}"
        )

    def to_dict(self):
        return {
            "number": self.number,
            "airline": self.airline,
            "departure": self.departure,
            "arrival": self.arrival,
            "status": self.status,
            "aircraft": self.aircraft,
            "altitude": self.altitude,
            "speed": self.speed,
            "heading": self.heading,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "dep_time": self.dep_time,
            "arr_time": self.arr_time,
        }
