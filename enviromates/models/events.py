from enviromates.database.db import db
from datetime import datetime

class Events(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    img_before = db.Column(db.String, nullable=False)
    img_after = db.Column(db.String)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False, default=1)
    start_date = db.Column(db.Date, nullable=False, default=datetime.now())
    end_date = db.Column(db.Date, )

    def __init__(self):
        return f"{self.id}"