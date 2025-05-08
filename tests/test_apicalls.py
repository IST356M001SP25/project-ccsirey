import pytest 
import sys
import os
from code.apicalls import get_place_id, get_directions
from code.bart_stations import get_address_from_station

def test_get_place_id():
    address = "2000 Mission St, San Francisco, CA"
    place_id = get_place_id(address)
    assert isinstance(place_id, str)
    assert place_id.startswith("ChI")

def test_get_directions():
    station_from = "16th St Mission"
    station_to = "Ashby"
    
    result_driving = get_directions(station_from, station_to, mode="driving")
    result_transit = get_directions(station_from, station_to, mode="transit")

    assert isinstance(result_driving, str)
    assert isinstance(result_transit, str)
    assert any(char.isdigit() for char in result_driving)
    assert any(char.isdigit() for char in result_transit)