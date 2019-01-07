from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    user_tracks = db.relationship('UserTrack', backref='user', lazy=True)
    role = db.Column(db.String(10), index=True)

    def __repr__(self):
        return f"<User: {self.id} {self.name}>"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'


class UserTrack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False,)
    track_id = db.Column(db.Integer, db.ForeignKey('track.id'), nullable=False)

    def __repr__(self):
        return f"<User`s track: {self.user_id} {self.track_id}>"


class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)
    spotify_link = db.Column(db.Text, nullable=True)
    youtube_link = db.Column(db.Text, nullable=True)
    image_link = db.Column(db.Text, nullable=True)
    user_tracks = db.relationship('UserTrack', backref='track', lazy=True)
    track_us_charts = db.relationship('UsChart', backref='user', lazy=True)
    track_uk_charts = db.relationship('UkChart', backref='user', lazy=True)

    def __repr__(self):
        return f"<{self.id} '{self.title}' - {self.artist}>"


class UsChart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_id = db.Column(db.Integer, db.ForeignKey('track.id'), nullable=False)
    date = db.Column(db.Text, nullable=False)
    rank = db.Column(db.Integer, nullable=False)

    # def __repr__(self):
    #     return f"<{self.id} {self.date} {self.rank}>"


class UkChart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_id = db.Column(db.Integer, db.ForeignKey('track.id'), nullable=False)
    date = db.Column(db.Text, nullable=False)
    rank = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<{self.id} {self.date} {self.rank}>"
