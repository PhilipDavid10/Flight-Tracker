import json
import os
from models import Flight

MAX_HISTORY = 20

def save_history(flight):
    if os.path.exists("data/history.json"):
        with open("data/history.json", "r") as file:
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

    with open("data/history.json", "w") as file:
        json.dump(history,file,indent=4)

def load_history():
    with open ("data/history.json", "r") as file:
        history = json.load(file)

    return history