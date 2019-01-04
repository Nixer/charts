import sqlite3
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
import datetime
import calendar
import billboard


def last_sunday(day):
    # day = input("Input date (Y-m-d):")
    sunday = datetime.datetime.strptime(day, "%Y-%m-%d")
    one_day = datetime.timedelta(days=1)

    while sunday.weekday() != calendar.SUNDAY:
        sunday -= one_day

    return sunday.strftime("%Y-%m-%d")


def all_sundays(year):
    """Return list of Sunday`s dates on particular year"""
    return pd.date_range(start=str(year), end=str(year+1), freq='W-SUN').strftime('%Y%m%d').tolist()


def add_json_chart_to_db(chart, country):
    if country == "us":
        chart_db = "us_chart"
    elif country == "uk":
        chart_db = "uk_chart"
    else:
        print("Wrong country name!")
    for date in chart.keys():
        for track in chart[date]:
            c.execute("SELECT id FROM track WHERE title = ? AND artist = ?",
                      (track['title'], track['artist']))
            data = c.fetchone()
            if data is None:
                c.execute("INSERT INTO track (title, artist) VALUES (?,?)",
                          (track['title'], track['artist']))
                c.execute(f"INSERT INTO {chart_db} (track_id, date, rank) VALUES (?,?,?)",
                          (c.lastrowid, date, track['rank']))
            else:
                c.execute(f"SELECT id FROM {chart_db} WHERE date = ? AND rank = ?",
                          (date, track['rank']))
                data_chart = c.fetchone()
                if data_chart is None:
                    c.execute(f"INSERT INTO {chart_db} (track_id, date, rank) VALUES (?,?,?)",
                              (data[0], date, track['rank']))
                else:
                    pass
        conn.commit()

    c.close()
    conn.close()


def parse_uk_chart(dates):
    uk_chart = {}
    try:
        for date in dates:
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
            uk_chart[f"{date[:4]}-{date[4:6]}-{date[6:]}"] = li
    except:
        pass
    return uk_chart


def get_chart(date):
    """Return Billboard chart object on particular date."""
    return billboard.ChartData('hot-100', date=date)


def parse_us_chart(dates):
    us_charts = {}
    for date in dates:
        try:
            chart = get_chart(f"{date[:4]}-{date[4:6]}-{date[6:]}")
            li = [
                {
                    "title": ch.title,
                    "artist": ch.artist,
                    "rank": ch.rank
                } for ch in chart
            ]
            us_charts[f"{date[:4]}-{date[4:6]}-{date[6:]}"] = li
        except:
            pass
    return us_charts


all_date = all_sundays(2018)

conn = sqlite3.connect("../webapp.db")
c = conn.cursor()
c.execute("SELECT MAX(id) AS id, date FROM us_chart")
last_actual_date = (last_sunday(datetime.datetime.today().strftime('%Y-%m-%d'))).replace("-", "")
latest_date_db = (c.fetchone()[-1]).replace("-", "")

dates_to_parse = all_date[all_date.index(latest_date_db) + 1:]
print(dates_to_parse)

# uk_chart = parse_uk_chart(dates_to_parse)
us_chart = parse_us_chart(dates_to_parse)

# print(uk_chart)
print(us_chart)
# add_json_chart_to_db(uk_chart, "uk")

add_json_chart_to_db(us_chart, "us")
