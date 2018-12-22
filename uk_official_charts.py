import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.officialcharts.com/charts/singles-chart/20181123/7501/")
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.find("table", {"class": "chart-positions"}))
