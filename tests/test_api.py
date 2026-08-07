from unittest.mock import patch
from api import get_flight_by_number
import requests

@patch("api.requests.get")
def test_get_flight_by_number_success(mock_get):
    mock_get.return_value.json.return_value = {
        "response": {
            "flight_iata": "AA100"
        }
    }

    result = get_flight_by_number("AA100")

    assert result["response"]["flight_iata"] == "AA100"

@patch("api.requests.get")
def test_get_flight_by_number_not_found(mock_get):
    mock_get.return_value.json.return_value = {
        "error": {
            "message": "Flight not found"
        }
    }

    result = get_flight_by_number("INVALID")

    assert result is None

@patch("api.requests.get")
def test_api_failure(mock_get):
    mock_get.side_effect = requests.RequestException()

    result = get_flight_by_number("AA100")

    assert result is None

@patch("api.requests.get")
def test_api_request_parameters(mock_get):
    mock_get.return_value.json.return_value = {
        "response": {}
    }

    get_flight_by_number("AA100")

    mock_get.assert_called_once()

    args, kwargs = mock_get.call_args

    assert kwargs["params"]["flight_iata"] == "AA100"