from flask import Blueprint
from flask_cors import cross_origin

main_routes = Blueprint("main", __name__)


@main_routes.route('/', methods=['GET'])
@cross_origin()
def index():
	return "Api root route."

