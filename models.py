class Flight():
    def __init__(self, number, airline, departure=None, arrival=None, status=None):
        self.number = number
        self.airline = airline
        self.departure = departure
        self.arrival = arrival
        self.status = status