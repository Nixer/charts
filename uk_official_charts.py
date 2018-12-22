import requests
import pandas as pd
from bs4 import BeautifulSoup


def all_sundays(year):
    return pd.date_range(start=str(year), end=str(year+1), freq='W-SUN').strftime('%Y%m%d').tolist()


for year in range(2018, 2019):
    try:
        for date in all_sundays(year):
            r = requests.get(f"https://www.officialcharts.com/charts/singles-chart/{date}/7501/")
            soup = BeautifulSoup(r.text, 'html.parser')
            print(soup.find("table", {"class": "chart-positions"}))
    except:
        pass
