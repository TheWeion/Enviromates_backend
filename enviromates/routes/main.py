from flask import Blueprint
from flask_cors import cross_origin,CORS

main_routes = Blueprint("main", __name__)
CORS(main_routes)


@main_routes.route('/', methods=['GET',"POST","PUT","PATCH","DELETE"])
@cross_origin()
def index():
	return "Api root route."

