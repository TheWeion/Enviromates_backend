from flask import Blueprint, request, redirect, jsonify
import jwt
import bcrypt
import string
from ..database.db import db
from ..models.user import Users

users_routes = Blueprint("user", __name__)

def hashPassword(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verifyPassword(password,hashedPassword):
    return bcrypt.checkpw(password.encode('utf-8'), hashedPassword)

def generateToken(user_id):
    return jwt.encode({'user_id': user_id}, 'secret', algorithm='HS256').decode('utf-8')

def verifyToken(token):
    try:
        return jwt.decode(token, 'secret', algorithms=['HS256'])
    except:
        return False

@users_routes.route("/", methods=["GET","POST"])
def auth_handler():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashedPassword = hashPassword(password)
        return f"user created: username:{username} password:{hashedPassword}"
    else:
        username = request.form["username"]
        password = request.form["password"]
        token = generateToken(username)
        return jsonify({"token":token})
        
@users_routes.route("/login", methods=["POST"])
def login_handler():
    username = request.form["username"]
    password = request.form["password"]
    db_user = db.Query.filter_by(username=username).first()
    
    if verifyPassword(password, db_user["password"]):
        token = generateToken(username)
        return jsonify({"token": token})
    else:
        return "Invalid username or password"
        
@users_routes.route("/register", methods=["POST"])
def register_handler():
    try:
        username = request.form["username"]
        password = request.form["password"]
        first_name = request.form["first-name"]
        last_name = request.form["last-name"]
        email = request.form["email"]
        hashedPassword = hashPassword(password)

        new_user = Users(username=username, password=hashedPassword, first_name=first_name, last_name=last_name, email=email)
        db.session.add(new_user)
        db.session.commit()
    except:
        return jsonify({"message":"Something went wrong on your end."}), 500
    
@users_routes.route("/test", methods=["GET"])
def test_route():
    return jsonify({"username":"username"}), 200