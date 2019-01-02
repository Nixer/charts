import requests
import pandas as pd
from bs4 import BeautifulSoup
import json


def all_sundays(year):
    """Return list of Sunday`s dates on particular year"""
    return pd.date_range(start=str(year), end=str(year+1), freq='W-SUN').strftime('%Y%m%d').tolist()


charts = {}
"""Write all UK Official charts for past 60 years to json file"""
for year in range(1958, 2019):
    try:
        for date in all_sundays(year):
            r = requests.get(f"https://www.officialcharts.com/charts/singles-chart/{date}/7501/")
            soup = BeautifulSoup(r.text, 'html.parser')
            positions = soup.findAll("span", {"class": "position"})
            titles = soup.findAll("div", {"class": "title"})
            artists = soup.findAll("div", {"class": "artist"})
            li = [
                {
                    "title": (titles[i].get_text()).strip().title(),
                    "artist": (artists[i].get_text()).strip().title(),
                    "rank": int((positions[i].get_text()).strip())
                } for i in range(len(positions))
            ]
            charts[f"{date[:4]}-{date[4:6]}-{date[6:]}"] = li
    except:
        pass

with open("uk_charts.json", "w+") as file:
    file.write(json.dumps(charts))
