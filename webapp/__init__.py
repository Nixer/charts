from flask import Flask, render_template
from open_charts_json import open_chart


app = Flask(__name__)

@ app.route("/")
def index():
    us = 'billboard_sample.json'
    uk = 'ukcharts_sample.json'
    us_chart = open_chart(us)
    uk_chart = open_chart(uk)
    current_top_us = sorted(us_chart.items())[-1]
    current_top_uk = sorted(uk_chart.items())[-1]
    return render_template('index.html', us_chart=us_chart, uk_chart =uk_chart, current_top_us=current_top_us, current_top_uk=current_top_uk)

@ app.route("/search_result")
def search_result():
    return render_template("search_result.html")

@ app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run()

