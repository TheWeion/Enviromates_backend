from flask import Blueprint, request, jsonify
from enviromates.database.db import db
from enviromates.models.events import Events

events_routes = Blueprint("events", __name__)

@events_routes.route("/", methods=["GET","POST"])
# Get list of events from database
def event_handler():
	if request.method == "GET":
		try:
			events = Events.query.all()
			return jsonify({"events":[event.serialize() for event in events]})
		except:
			return "No events found.",200
	elif request.method == "POST":
		try:
			title = request.form["title"]
			description = request.form["description"]
			difficulty = request.form["difficulty"]
			start_date = request.form["start-date"]
			latitude = request.form["latitude"]
			longitude = request.form["longitude"]
			img_before = request.form["img-before"]
			new_event = Events(title=title, description=description, difficulty=difficulty, start_date=start_date, latitude=latitude, longitude=longitude, img_before=img_before)
			db.session.add(new_event)
			db.session.commit()
			return "Event added."
		except:
			return 'could not add event to database.'
	else:
		return "Invalid request."

        
@events_routes.route("/<event_id>", methods=["GET","PUT","DELETE"])
def event_id_handler(event_id):
	if request.method == "GET":
		event = Events.query.filter_by(id=event_id).first()
		return jsonify(event.serialize())
	elif request.method == "PUT":
		event = Events.query.filter_by(id=event_id).first()
		event.title = request.form["title"]
		event.description = request.form["description"]
		event.difficulty = request.form["difficulty"]
		event.start_date = request.form["start-date"]
		event.latitude = request.form["latitude"]
		event.longitude = request.form["longitude"]
		event.img_after = request.form["img-after"]
		db.session.commit()
		return jsonify({"message":"Event updated."})
	elif request.method == "DELETE":
		event = Events.query.filter_by(id=event_id).first()
		db.session.delete(event)
		db.session.commit()
		return jsonify({"message":"Event deleted."})
	else:
		return jsonify({"message":"Invalid request."})