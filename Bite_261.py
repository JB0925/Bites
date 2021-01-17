import json
from dataclasses import dataclass
from datetime import datetime
from math import acos, cos, radians, sin, pi, atan2, sqrt
import os
from pathlib import Path
from urllib.request import urlretrieve

from dateutil.parser import parse

URL = "https://bites-data.s3.us-east-2.amazonaws.com/pycons-europe-2019.json"
RESPONSES = "https://bites-data.s3.us-east-2.amazonaws.com/nominatim_responses.json"

tmp = Path('C:/Users/superuser/Bites')
pycons_file = tmp / "pycons-europe-2019.json"
nominatim_responses = tmp / "nominatim_responses.json"

if not pycons_file.exists() or not nominatim_responses.exists():
    urlretrieve(URL, pycons_file)
    urlretrieve(RESPONSES, nominatim_responses)


@dataclass
class PyCon:
    name: str
    city: str
    country: str
    start_date: datetime
    end_date: datetime
    URL: str
    lat: float = None
    lon: float = None


@dataclass
class Trip:
    origin: PyCon
    destination: PyCon
    distance: float


def _get_pycons():
    """Helper function that retrieves required PyCon data
       and returns a list of PyCon objects
    """
    with open(pycons_file, "r", encoding="utf-8") as f:
        return [
            PyCon(
                pycon["name"],
                pycon["city"],
                pycon["country"],
                parse(pycon["start_date"]),
                parse(pycon["end_date"]),
                pycon["url"],
            )
            for pycon in json.load(f)
        ]


def _km_distance(origin, destination):
    """ Helper function that retrieves the air distance in kilometers for two pycons """
    lon1, lat1, lon2, lat2 = map(
        radians, [origin.lon, origin.lat, destination.lon, destination.lat]
    )
    return 6371 * (
        acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
    )


# Your code #
def update_pycons_lat_lon(pycons):
    """
    Update the latitudes and longitudes based on the city and country
    the PyCon takes places. Use requests from the Nominatim API stored in the
    nominatim_responses json file.
    """
    i = 0

    with open('nominatim_responses.json') as f:
        reader = json.load(f)
        for row, value in reader.items():
            latitude, longitude = float(value[0]['lat']), float(value[0]['lon'])
            pycons[i].lat, pycons[i].lon = latitude, longitude
            i += 1
    
    return pycons


def create_travel_plan(pycons):
    """
    Create your travel plan to visit all the PyCons.
    Assume it's now the start of 2019!
    Return a list of Trips with each Trip containing the origin PyCon,
    the destination PyCon and the travel distance between the PyCons.
    """
    trips = []

    pycons = sorted(pycons, key=lambda x: x.start_date)
    for i in range(len(pycons)-1):
        var1, var2 = pycons[i].lat * pi / 180, pycons[i+1].lat * pi / 180
        var3, var4 = (pycons[i+1].lat - pycons[i].lat) * pi / 180, (pycons[i+1].lon - pycons[i].lon) * pi / 180
        calc1 = sin(var3/2) * sin(var3/2) + cos(var1) * cos(var2) * sin(var4/2) * sin(var4/2)
        calc2 = 2 * atan2(sqrt(calc1), sqrt(1-calc1))
        distance = 6_371 * calc2

        t = Trip(origin=pycons[i].name, destination=pycons[i+1].name, distance=distance)
        trips.append(t)
    
    return trips
        
    
def total_travel_distance(journey):
    """
    Return the total travel distance of your PyCon journey in kilometers
    rounded to one decimal.
    """
    total_distance = 0

    for trip in journey:
        total_distance += trip.distance
    
    return round(total_distance, 1)



pycons = _get_pycons()
updated_pycons = update_pycons_lat_lon(pycons)
trips = create_travel_plan(updated_pycons)
print(total_travel_distance(trips))
