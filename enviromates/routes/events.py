
from flask import Blueprint, request, jsonify
from enviromates.database.db import db
from enviromates.models.events import Events

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
		print("events post hit.")
		try:
			title = request.form["title"]
			description = request.form["description"]
			difficulty = request.form["difficulty"]
			latitude = request.form["latitude"]
			longitude = request.form["longitude"]
			img_before = request.form["img-before"]
			new_event = Events(title=title, description=description, difficulty=difficulty, latitude=latitude, longitude=longitude, img_before=img_before)
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

		event = Events.query.filter_by(id=event_id).first()
		event.title = request.form.get("title") or event.title
		event.description = request.form.get("description") or event.description
		event.difficulty = request.form.get("difficulty") or event.difficulty
		event.start_date = request.form.get("start-date") or event.start_date
		event.latitude = request.form.get("latitude") or event.latitude
		event.longitude = request.form.get("longitude") or event.longitude
		event.img_after = request.form.get("img-after") or event.img_after
		db.session.commit()
		return jsonify({"message":"Event updated."})

################################################## DELETE ONE event
	elif request.method == "DELETE":
		event = Events.query.filter_by(id=event_id).first()
		db.session.delete(event)
		db.session.commit()
		return jsonify({"message":"Event deleted."})
	else:
		return jsonify({"message":"Invalid request."})