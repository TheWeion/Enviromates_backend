from enviromates.database.db import db
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    cur_points = db.Column(db.Integer, nullable=False, default=0)
    events_attended_by_user = db.Column(db.Integer, default=0)
    events_hosted_by_user = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    
    def output(self):
        return {
            "id":self.id,
            "username":self.username,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "email":self.email,
            "cur_points":self.cur_points,
            "events_attended_by_user":self.events_attended_by_user,
            "events_hosted_by_user":self.events_hosted_by_user,
            "created_at":self.created_at,
            }