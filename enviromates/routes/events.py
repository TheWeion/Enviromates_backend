
# ─── Imports ────────────────────────────────────────────────────────────────────

from flask import Blueprint, request, jsonify
from enviromates.database.db import db
from enviromates.models.events import Events
from enviromates.models.user import Users
from enviromates.models.lobby import Lobby
from enviromates.helpers.auth_helpers import verifyToken

# ─── Globals ────────────────────────────────────────────────────────────────────

events_routes = Blueprint("events", __name__)

# ────────────────────────────────────────────────────────────────────────────────

# ─── Event: GET And POST Routes ──────────────────────────────────────────────────

@events_routes.route("/", methods=["GET","POST"])
def event_handler():
	if request.method == "GET":
		try:
			events = Events.query.all()
			events_list=[]
			for event in events:
				events_list.append(event.output())
			return jsonify({"events":events_list})
		except Exception as e:
			return f"{e}",200


	elif request.method == "POST":
		try:
			# auth the user
			token = request.form["accesstoken"]
			username = verifyToken(token)["user_username"]

			user = Users.query.filter_by(username=username).first()
			title = request.form.get("title")
			author_id = user.output()["id"]
			description = request.form.get("description")
			difficulty = request.form.get("difficulty")
			latitude = request.form.get("latitude")
			longitude = request.form.get("longitude")
			img_before = request.form.get("img-before")

			new_event = Events(title=title,author_id=author_id, description=description, difficulty=difficulty, latitude=latitude, longitude=longitude, img_before=img_before)
			db.session.add(new_event)
			db.session.commit()
			event_id = Events.query.filter_by(id=user.id).first().id
			new_lobby = Lobby(user_id=author_id, event_id=event_id, has_attended=False)
			db.session.add(new_lobby)
			db.session.commit()
			return jsonify({"success":"true","message":"event created.","data":new_event.output()})
		except Exception as e:
			return f"{e}"
	else:
		return "Invalid request."

# ─── Event: Modify Routes By Id ──────────────────────────────────────────────────

@events_routes.route("/<event_id>", methods=["GET","PUT","DELETE"])
def event_id_handler(event_id):

	if request.method == "GET":
		event = Events.query.filter_by(id=event_id).first()
		return jsonify({"event":event.output(), "attendees": len(Lobby.get_lobby_by_event_id(event_id))})

	elif request.method == "PUT":

		# Auth the user account
		try:
			token = request.headers.get("accesstoken")
			decoded_token = verifyToken(token)
			username = decoded_token["user_username"]
			user = Users.query.filter_by(username=username).first()
			event = Events.query.filter_by(id=event_id).first()
		except:
			return jsonify({"success":"False","message":"Something went wrong during event update."})
		if event.author_id == user.id:

			event.title = request.form.get("title") or event.title
			event.description = request.form.get("description") or event.description
			event.difficulty = request.form.get("difficulty") or event.difficulty
			event.start_date = request.form.get("start-date") or event.start_date
			event.latitude = request.form.get("latitude") or event.latitude
			event.longitude = request.form.get("longitude") or event.longitude
			event.img_after = request.form.get("img-after") or event.img_after
			db.session.commit()
			return jsonify({"message":"Event updated."})
		else:
			if request.form.get("join") == "true":
				join_lobby = Lobby(user_id=user.id, event_id=event_id)
				incr_attendence = Users.query.filter_by(id=user.id).update({"events_attended_by_user":user.events_attended_by_user+1})
				db.session.add(join_lobby)
				db.session.add(incr_attendence)
				db.session.commit()
				return jsonify({"message":"You have joined the lobby."})
			elif request.form.get("leave") == "true":
				lobby = Lobby.query.filter_by(user_id=user.id, event_id=event_id).first()
				decr_attendence = Users.query.filter_by(id=user.id).update({"events_attended_by_user":user.events_attended_by_user-1})
				db.session.add(decr_attendence)
				db.session.delete(lobby)
				db.session.commit()
				return jsonify({"message":"You have left the lobby."})
			else:
				return jsonify({"message":"Something went wrong during event update."})

################################################## DELETE ONE event
	elif request.method == "DELETE":
		event = Events.query.filter_by(id=event_id).first()
		db.session.delete(event)
		db.session.commit()
		return jsonify({"message":"Event deleted."})
	else:
		return jsonify({"message":"Invalid request."})
