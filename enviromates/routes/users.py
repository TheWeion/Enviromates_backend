from flask import Blueprint, request, jsonify



# database tables
from enviromates.database.db import db
from enviromates.models.user import Users

# helper functions for auth
from enviromates.helpers.auth_helpers import hashPassword, generateToken, verifyPassword

# Blurprint prefix setup
users_routes = Blueprint("users", __name__)


################################################## GET ALL users
@users_routes.route("/", methods=["GET"])
def auth_handler():
        users_list=[]
        users = Users.query.all()
        for user in users:
            users_list.append(user.output())
        return jsonify({"users":users_list})


################################################## Login user, return access token
@users_routes.route("/login", methods=["POST"])
def login_handler():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db_user = Users.query.filter_by(username=username).first()
    if verifyPassword(password, db_user.password):
        token = generateToken(username)
        return jsonify({"success":"True","token":token})
    else:
        return "Invalid username or password"
        
################################################## Register new user
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
        return jsonify({"success":"true","message":"account created successfully.","user":new_user.output()})

    except Exception as e:
        return f"{e}" 

################################################## User CRUD by username
@users_routes.route("/<username>", methods=["GET", "PUT", "DELETE"])
def user_handler(username):

################################################## DELETE USER
    if request.method == "DELETE":
        user = Users.query.filter_by(username=username).first()
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message":"User deleted."})

################################################## EDIT USER
    elif request.method == "PUT":
        user = Users.query.filter_by(username=username).first()
        user.username = request.form.get("username") or user.username
        user.password = hashPassword(request.form.get("password")) or user.password
        user.first_name = request.form.get("first-name") or user.first_name
        user.last_name = request.form.get("last-name") or user.last_name
        user.email = request.form.get("email") or user.email
        db.session.commit()
        return jsonify({"message":"User updated."})

################################################## GET USER information
    elif request.method == "GET":
        user = Users.query.filter_by(username=username).first()
        return jsonify({"user":user.output()})
    else:
        return "Not found.",200
    
    
    
    
    
    
    
    
    
      
