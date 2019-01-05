import json
import os

_location_ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def open_chart(country):
    """Opens chart json file"""
    with open(f'{_location_}/{country}') as f:
        chart = json.loads(f.read())
        return chart


