import json
import os
from models import Flight
from pathlib import Path

MAX_HISTORY = 20
HISTORY_FILE = Path(__file__).parent / "history.json"

def save_history(flight, history_file=HISTORY_FILE):
    if history_file.exists():
        with open(history_file, "r") as file:
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

    with open(history_file, "w") as file:
        json.dump(history,file,indent=4)

def load_history(history_file=HISTORY_FILE):
    if history_file.exists():
        try: 
            with open (history_file, "r") as file:
                history = json.load(file)
        except json.JSONDecodeError:
            return []
    else:
        return []

    return history