from flask import Flask, render_template
from open_charts_json import open_chart
import datetime
from dateutil import relativedelta
from webapp.forms import DateForm


app = Flask(__name__)

@ app.route("/")
def index():
    # date_form = DateForm()
    years = [year for year in range(1958, 2020,1)]
    days = [day for day in range(1,32,1)]
    us = 'billboard_sample.json'
    uk = 'ukcharts_sample.json'
    us_chart = open_chart(us)
    uk_chart = open_chart(uk)
    current_top_us = sorted(us_chart.items())[-1]
    current_top_uk = sorted(uk_chart.items())[-1]
    return render_template('index.html', days=days, years=years, us_chart=us_chart,
    uk_chart =uk_chart, current_top_us=current_top_us, current_top_uk=current_top_uk)

@ app.route("/search_result")
def search_result():
    user_date = "user input from index page "
    #user_date = datetime.datetime.now()
    start = user_date - datetime.timedelta((user_date.weekday() + 1) % 7)
    sat = start + relativedelta.relativedelta(weekday=relativedelta.SA(-1))
    user_sunday_date = sat + relativedelta.relativedelta(weekday=relativedelta.SU(-1))

    return render_template("search_result.html", user_sunday_date=user_sunday_date)

@ app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run()

