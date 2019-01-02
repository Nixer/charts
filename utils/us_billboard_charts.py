import billboard
import pandas as pd
import json


def all_sundays(year):
    """Return list of Sunday`s dates on particular year"""
    return pd.date_range(start=str(year), end=str(year+1), freq='W-SUN').strftime('%Y-%m-%d').tolist()


def get_chart(date):
    """Return Billboard chart object on particular date."""
    return billboard.ChartData('hot-100', date=date)


charts = {}
"""Write all Billboard charts for past 60 years to json file"""
for year in range(1958, 2019):
    for date in all_sundays(year):
        try:
            chart = get_chart(date)
            li = [
                {
                    "title": ch.title,
                    "artist": ch.artist,
                    "rank": ch.rank
                } for ch in chart
            ]
            charts[date] = li
        except:
            pass
with open("us_charts.json", "w+") as file:
    file.write(json.dumps(charts))
