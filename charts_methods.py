import json


def open_chart_us():
    """Opens chart json file"""
    with open('bob.json') as f:
        us_chart = json.loads(f.read())
        return us_chart


if __name__ == "__main__":

    us_chart = open_chart_us()

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