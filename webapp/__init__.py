from flask import Flask, render_template
from charts_methods import open_chart_us


app = Flask(__name__)

@ app.route("/")
def index():

    us_chart = open_chart_us()

    return render_template('index.html', us_chart=us_chart)


if __name__ == "__main__":
    app.run()

