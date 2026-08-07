import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

FLIGHT_URL = "https://airlabs.co/api/v9/flight"
MULTIPLE_FLIGHTS_URL = "https://airlabs.co/api/v9/flights"
AIRPORTS_URL = "https://airlabs.co/api/v9/airports"