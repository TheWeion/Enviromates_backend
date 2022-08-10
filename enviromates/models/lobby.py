from enviromates.database.db import db
from .user import Users
from .events import Events

class Lobby(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey(Users.id))
	event_id = db.Column(db.Integer, db.ForeignKey(Events.id))
	has_attended = db.Column(db.Boolean, nullable=False, default=False)
 
	def __init__(self, user_id, event_id, has_attended):
		self.user_id = user_id
		self.event_id = event_id
		self.has_attended = has_attended
        
	def __repr__(self):
		return f"<Lobby {self.id}>"
    
	@classmethod
	def get_lobby(cls, id):
		return cls.query.filter_by(id=id).first()
	@classmethod
	def get_lobby_by_user_id(cls, user_id):
		return cls.query.filter_by(user_id=user_id).first()
	@classmethod
	def get_lobby_by_event_id(cls, event_id):
		return cls.query.filter_by(event_id=event_id).first()
	@classmethod
	def get_lobby_by_user_id_and_event_id(cls, user_id, event_id):
		return cls.query.filter_by(user_id=user_id, event_id=event_id).first()
    