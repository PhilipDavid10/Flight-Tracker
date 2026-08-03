import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

FLIGHT_URL = "https://airlabs.co/api/v9/flight"
AIRPORT_URL = "https://airlabs.co/api/v9/flights"