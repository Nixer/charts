import json
import os

_location_ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def open_chart(country):
    """Opens chart json file"""
    with open(f'{_location_}/{country}') as f:
        chart = json.loads(f.read())
        return chart


if __name__ == "__main__":

    us_chart = open_chart()

    current = sorted(us_chart.items())[-1]
    for key,value in us_chart.items():
        if key == current[0]:
            for song in value:
                rank = song['rank']
                title = song['title']
                artist = song['artist']
                print(rank,title, artist)
        else:
            print("No data found")