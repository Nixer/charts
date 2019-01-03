from flask import Flask, render_template, request
from open_charts_json import open_chart
import datetime
from dateutil import relativedelta
# from webapp.forms import DateForm
from webapp.model import *
from utils.last_sunday import last_sunday

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @ app.route("/", methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            years = [year for year in range(1958, 2020, 1)]
            days = [day for day in range(1, 32, 1)]
            data = request.form.to_dict()
            day = data['day']
            month = data['month']
            year = data['year']
            sunday = last_sunday(f"{year}-{month}-{day}")
            current_top_us = []
            current_top_uk = []
            chart_for_date_uk = UkChart.query.filter_by(date=sunday).order_by(UkChart.rank).all()
            chart_for_date_us = UsChart.query.filter_by(date=sunday).order_by(UsChart.rank).all()
            for c in chart_for_date_uk:
                track = Track.query.get(c.track_id)
                current_top_uk.append({'title': track.title, 'artist': track.artist, 'rank': c.rank})
            for c in chart_for_date_us:
                track = Track.query.get(c.track_id)
                current_top_us.append({'title': track.title, 'artist': track.artist, 'rank': c.rank})
            # return f"{friday}: {charts}"
            return render_template('index.html', days=days, years=years, date=sunday,
                                   current_top_us=current_top_us, current_top_uk=current_top_uk)
        else:
            years = [year for year in range(1958, 2020, 1)]
            days = [day for day in range(1, 32, 1)]
            us = 'us_billboard_sample.json'
            uk = 'ukcharts_sample.json'
            us_chart = open_chart(us)
            uk_chart = open_chart(uk)
            current_top_us = (sorted(us_chart.items())[-1])[-1]
            current_top_uk = (sorted(uk_chart.items())[-1])[-1]
            date = (sorted(us_chart.items())[-1])[0]
            return render_template('index.html', days=days, years=years, date=date,
                                   current_top_us=current_top_us, current_top_uk=current_top_uk)

    # @ app.route("/search_result")
    # def search_result():
    #     user_date = "user input from index page "
    #     #user_date = datetime.datetime.now()
    #     start = user_date - datetime.timedelta((user_date.weekday() + 1) % 7)
    #     sat = start + relativedelta.relativedelta(weekday=relativedelta.SA(-1))
    #     user_sunday_date = sat + relativedelta.relativedelta(weekday=relativedelta.SU(-1))
    #
    #     return render_template("search_result.html", user_sunday_date=user_sunday_date)

    @ app.route("/login")
    def login():
        return render_template("login.html")

    @app.route("/signup")
    def signup():
        return render_template("signup.html")

    return app

