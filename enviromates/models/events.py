from dataclasses import dataclass
from enviromates.database.db import db
from datetime import datetime

@dataclass
class Events(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    latitude = db.Column(db.String, nullable=False)
    longitude = db.Column(db.String, nullable=False)
    img_before = db.Column(db.String, nullable=False)
    img_after = db.Column(db.String)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    difficulty = db.Column(db.String, nullable=False, default="1")
    start_date = db.Column(db.String, nullable=False, default=datetime.now())
    end_date = db.Column(db.String)

    def output(self):
        return{
            "id" : self.id,
            "latitude" : self.latitude,
            "longitude" : self.longitude,
            "img_before" : self.img_before,
            "img_after" : self.img_after,
            "title" : self.title,
            "description" : self.description,
            "difficulty" : self.difficulty,  
            "start_date" : self.start_date,
            "end_date" : self.end_date,
        }