"""Tests for flight_paths.py."""

import pytest
from flight_paths import *

TEST_AIRPORTS = [{"city": "Louisiana", "destination_cities": ["Frank's Red Hot", "Crystal"], 'lat_lon': [0.0, 0.0]},
{"city": "Crystal", "destination_cities": ["Lousiana"], 'lat_lon': [10.0, 0.0]},
{"city": "Frank's Red Hot", "destination_cities": ["Sriracha", "Louisiana"], 'lat_lon': [0.0, 0.0]},
{"city": "Sriracha", "destination_cities": ["Crystal", "Frank's Red Hot"], 'lat_lon': [-10, 0.0]}]


@pytest.fixture
def test_world():
    """Make fake cities."""
    dictify_airport_data(TEST_AIRPORTS)

def test_get_data_from_json_file():
    """Test that the airport-data JSON file imports."""
    data = get_data_from_json_file()
    assert type(data) == list

def test_data_converted_to_dict():
    """Test that read data converts to dictionary."""
    data = get_data_from_json_file()
    airports_dict = dictify_airport_data(data)
    assert type(airports_dict) == dict

def test_fake_airport_nondistance():
    """Test that distance between two airports at same location is 0."""
    assert return_shortest_route("Louisiana", "Frank's Red Hot", TEST_AIRPORTS) == "0.0 ['Louisiana', \"Frank\'s Red Hot\"]"
