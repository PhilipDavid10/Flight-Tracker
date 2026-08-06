import json
import os
from models import Flight
from pathlib import Path

MAX_HISTORY = 20
HISTORY_FILE = Path(__file__).parent / "history.json"

def save_history(flight):
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)
    else:
        history = []

    # get new flight
    new_flight = flight.to_dict()

    # check if flight already in search history
    history = [old_flight for old_flight in history
               if old_flight.get("number") != new_flight.get("number")]

    # add new flight
    history.append(new_flight)

    # keep only newest searches
    history = history[-MAX_HISTORY:]

    with open(HISTORY_FILE, "w") as file:
        json.dump(history,file,indent=4)

def load_history():
    with open (HISTORY_FILE, "r") as file:
        history = json.load(file)

    return history