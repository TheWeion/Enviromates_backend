from ..database.db import db
from datetime import datetime

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False, required=True)
    longitude = db.Column(db.Float, nullable=False, required=True)
    img_before = db.Column(db.String, nullable=False, required=True)
    img_after = db.Column(db.String, nullable=False, required=True)
    title = db.Column(db.String, nullable=False, required=True)
    description = db.Column(db.String, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False, required=True, default=1)
    start_date = db.Column(db.Date, nullable=False, required=True, default=datetime.datetime.now())
    end_date = db.Column(db.Date, nullable=False, required=True)
    user_list = db.relationship('Users', secondary='event_user', backref=db.backref('events', lazy='dynamic'))