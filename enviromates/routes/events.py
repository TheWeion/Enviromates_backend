from flask import Blueprint, request, redirect, jsonify
from ..database.db import db
from ..models.user import Users

event_routes = Blueprint("events", __name__)

event_routes.route("/", methods=["GET","POST"])
# Get list of events
