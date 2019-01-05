from flask import Flask, render_template, request
from utils.db_queries import get_records
from webapp.model import *
from utils.last_sunday import last_sunday


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @ app.route("/", methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            data = request.form.to_dict()
            day = data['day']
            month = data['month']
            year = data['year']
            sunday = last_sunday(f"{year}-{month}-{day}")
            days, years, current_top_us, current_top_uk = get_records(sunday)
            return render_template('index.html', days=days, years=years, date=sunday,
                                   current_top_us=current_top_us, current_top_uk=current_top_uk)
        else:
            latest_date_uk = (UkChart.query.get(db.session.query(db.func.max(UkChart.id)).first()[0])).date
            latest_date_us = (UsChart.query.get(db.session.query(db.func.max(UsChart.id)).first()[0])).date
            days, years, current_top_us, current_top_uk = get_records(latest_date_uk)
            return render_template('index.html', days=days, years=years, date=latest_date_uk,
                                   current_top_us=current_top_us, current_top_uk=current_top_uk)

    @ app.route("/login")
    def login():
        return render_template("login.html")

    @app.route("/signup")
    def signup():
        return render_template("signup.html")

    return app
