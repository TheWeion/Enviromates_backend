from enviromates import app
from waitress import serve

serve(app, port=8000, threads=8)