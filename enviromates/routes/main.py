from flask import Blueprint, request

main_routes = Blueprint("main", __name__)


@main_routes.route('/', methods=['GET', 'POST'])
def index():
	return "Api root route."

