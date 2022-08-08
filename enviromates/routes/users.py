from flask import Blueprint, request, jsonify

# database tables
from enviromates.database.db import db
from enviromates.models.user import Users

# helper functions for auth
from enviromates.helpers.auth_helpers import verifyPassword,generateToken,hashPassword

# Blurprint prefix setup
users_routes = Blueprint("users", __name__)


# G
@users_routes.route("/", methods=["POST"])
def auth_handler():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashedPassword = hashPassword(password)
        return jsonify({"message":f"user created: username:{username} password:{hashedPassword}"}),200
    else:
        return jsonify({"message","something went wrong."}),401
        # username = request.form["username"]
        # password = request.form["password"]
        # token = generateToken(username)
        # return jsonify({"token":token})
        
@users_routes.route("/login", methods=["POST","GET"])
def login_handler():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db_user = Users.query.filter_by(username=username).first()
    
        if verifyPassword(password, db_user.password):
            token = generateToken(username)
            # Response.headers.add("accesstoken", token)
            return "congratulations", 200
    else:
        return "Invalid username or password"
        
@users_routes.route("/register", methods=["POST"])
def register_handler():
    try:
        # check if username is already taken
        username = request.form["username"]
        password = request.form["password"]
        first_name = request.form["first-name"]
        last_name = request.form["last-name"]
        email = request.form["email"]
        hashedPassword = hashPassword(password)
        new_user = Users(username=username, password=hashedPassword, first_name=first_name, last_name=last_name, email=email)
        db.session.add(new_user)
        db.session.commit()
        found_user = Users.query.filter_by(username=username).first()
        print(found_user)
        return jsonify({"user":found_user})
    except Exception as e:
        return f"{e}" 



@users_routes.route("/<user_id>", methods=["GET", "PUT", "DELETE"])
def user_handler(user_id):
    if request.method == "DELETE":
        user = Users.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message":"User deleted."})
    elif request.method == "PUT":
        user = Users.query.filter_by(id=user_id).first()
        user.username = request.form["username"]
        user.password = hashPassword(request.form["password"])
        user.first_name = request.form["first-name"]
        user.last_name = request.form["last-name"]
        user.email = request.form["email"]
        db.session.commit()
        return jsonify({"message":"User updated."})
    elif request.method == "GET":

        user = Users.query.filter_by(id=user_id).first()
        return jsonify({"user":user.serialize()})
    else:
        return "Not found.",200
    
    
    
    
    
    
    
    
    
    
      
