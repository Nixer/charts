from webapp import db, create_app
from flask import Flask


# app = Flask(__name__)
# app.config.from_pyfile('config.py')
# db.init_app(app)

db.create_all(app=create_app())
