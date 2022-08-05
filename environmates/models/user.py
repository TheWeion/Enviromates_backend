from ..database.db import db
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hwid = db.Column(db.Integer, db.ForeignKey("hwid.id"), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    cur_points = db.Column(db.Integer, nullable=False, default=0)
    badges = db.Column(db.Integer, nullable=False, default=0)
    events_attended_by_user = db.Column(db.Integer, nullable=False, default=0)
    events_hosted_by_user = db.Column(db.Integer, nullable=False, default=0)
    events_list = db.relationship('Events', secondary='event_user', backref=db.backref('users', lazy='dynamic'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())