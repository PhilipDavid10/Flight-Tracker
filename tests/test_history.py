from data.history import save_history, load_history
from models import Flight


def test_save_history(tmp_path):
    history_file = tmp_path / "history.json"

    flight = Flight(
        number="AA100",
        airline="American Airlines",
        departure="JFK",
        arrival="LHR"
    )

    save_history(flight,history_file)

    history = load_history(history_file)

    assert len(history) == 1
    assert history[0]["number"] == "AA100"

def test_multiple_history_entries(tmp_path):
    history_file = tmp_path / "history.json"

    flights = [
        Flight("AA100","American Airlines"),
        Flight("WS1","westjet"),
        Flight("BA50","British Airways")
    ]

    for flight in flights:
        save_history(flight, history_file)

    history = load_history(history_file)

    assert len(history) == 3

def test_duplicates_move_to_end(tmp_path):
    history_file = tmp_path / "history.json"

    save_history(Flight("AA100","American Airlines"), history_file)
    save_history(Flight("WS1","Westjet"), history_file)
    save_history(Flight("BA50","British Airways"), history_file)
    save_history(Flight("WS1","Westjet"), history_file)

    history = load_history(history_file)

    assert len(history) == 3
    assert history[-1]["number"] == "WS1"

def test_max_history(tmp_path):
    history_file = tmp_path / "history.json"

    for i in range(25):

        flight = Flight(
            number = f"AA{i}",
            airline="Airline"
        )

        save_history(flight, history_file)

    history = load_history(history_file)

    assert len(history) == 20
    assert history[0]["number"] == "AA5"

def test_load_missing_history_file(tmp_path):
    history_file = tmp_path / "history.json"

    history = load_history(history_file)

    assert history == []

def test_corrupted_history_file(tmp_path):
    history_file = tmp_path / "history.json"

    history_file.write_text("invalid Json")

    history = load_history(history_file)

    assert history == []

def test_duplicate_updates_flight(tmp_path):
    history_file = tmp_path / "history.json"

    save_history(
        Flight(
            number="WS1",
            airline="Westjet",
            status="scheduled"
        ), history_file
    )

    save_history(
        Flight(
            number="WS1",
            airline="Westjet",
            status="en-route"
        ),history_file
    )

    history = load_history(history_file)

    assert len(history) == 1
    assert history[0]["status"] == "en-route"

def test_history_keeps_search_order(tmp_path):
    history_file = tmp_path / "history.json"

    save_history(Flight("AA100","American Airlines"),history_file)
    save_history(Flight("WS1","Westjet"),history_file)

    history = load_history(history_file)

    assert history[0]["number"] == "AA100"
    assert history[1]["number"] == "WS1"