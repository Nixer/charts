from flask import Flask, render_template
from open_charts_json import open_chart_us


app = Flask(__name__)

@ app.route("/")
def index():
    us_chart = open_chart_us()
    return render_template('index.html', us_chart=us_chart)

@ app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run()

