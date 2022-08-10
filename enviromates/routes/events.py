
from flask import Blueprint, request, jsonify
from enviromates.database.db import db
from enviromates.models.events import Events
from enviromates.models.user import Users

from enviromates.helpers.auth_helpers import verifyToken

events_routes = Blueprint("events", __name__)

@events_routes.route("/", methods=["GET","POST"])
def event_handler():
################################################## GET ALL events
	if request.method == "GET":
		try:
			events = Events.query.all()
			events_list=[]
			for event in events:
				events_list.append(event.output())
			return jsonify({"events":events_list})


			# return jsonify({"events":[event.serialize() for event in events]})
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
			print(f"user is", user.username)
			print("title is", title)
			print("author is",author_id)
			print("description is" , description)
			print("difficulty is", difficulty)
			print("img_before", img_before)
			new_event = Events(title=title,author_id=author_id, description=description, difficulty=difficulty, latitude=latitude, longitude=longitude, img_before=img_before)
			db.session.add(new_event)
			db.session.commit()
			return jsonify({"success":"true","message":"event created.","data":new_event.output()})
		except Exception as e:
			return f"{e}"
	else:
		return "Invalid request."


################################################## EVENT CRUD operations
@events_routes.route("/<event_id>", methods=["GET","PUT","DELETE"])
def event_id_handler(event_id):

################################################## GET ONE event information
	if request.method == "GET":
		event = Events.query.filter_by(id=event_id).first()
		return jsonify(event.output())


################################################## EDIT ONE event
	elif request.method == "PUT":

		# auth the user
		try:
			token = request.headers.get("accesstoken")
			decoded_token = verifyToken(token)
			username = decoded_token["user_username"]
			print(decoded_token)
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
			return jsonify({"success":"False","message":"something went wrong."})
################################################## DELETE ONE event
	elif request.method == "DELETE":
		event = Events.query.filter_by(id=event_id).first()
		db.session.delete(event)
		db.session.commit()
		return jsonify({"message":"Event deleted."})
	else:
		return jsonify({"message":"Invalid request."})