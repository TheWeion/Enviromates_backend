from dotenv import load_dotenv
from os import environ, getenv
from flask import Flask
from flask_cors import CORS

from enviromates.database.db import db
from enviromates.routes.main import main_routes
from enviromates.routes.users import users_routes
from enviromates.routes.events import events_routes

# Load environment variables

load_dotenv()

database_uri = environ.get('DATABASE_URL')

if 'postgres:' in database_uri:
    database_uri = database_uri.replace("postgres:", "postgresql:")

# Set up the app

app = Flask(__name__)
app.secret_key = getenv('SECRET_KEY')

app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
)

CORS(app)
db.app = app
db.init_app(app)

app.register_blueprint(main_routes)
app.register_blueprint(users_routes, url_prefix="/users")
app.register_blueprint(events_routes, url_prefix="/events")
## Main

if __name__ == "__main__":
    app.run(debug=True)