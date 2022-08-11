from flask import Blueprint, request, jsonify


# database tables
from enviromates.database.db import db
from enviromates.models.user import Users

# helper functions for auth
from enviromates.helpers.auth_helpers import hashPassword, generateToken, verifyPassword, verifyToken

# Blurprint prefix setup
users_routes = Blueprint("users", __name__)


################################################## user needs their data
@users_routes.route("/", methods=["POST"])
def get_user_data():
    if request.method == "POST":

        print(request.form["accesstoken"])
        try:
            token = request.form["accesstoken"]
            username = verifyToken(token)["user_username"]
            user = Users.query.filter_by(username=username).first()
            return jsonify({"success":"True","user":user.output()})
        except:
            return "auth failed."

################################################## Login user, return access token
@users_routes.route("/login", methods=["POST"])
def login_handler():

    if request.method == "POST":
        try:
            username = request.form["username"]
            password = request.form["password"]
            db_user = Users.query.filter_by(username=username).first()
            if verifyPassword(password, db_user.password):
                try :
                    token = generateToken(username)
                    return jsonify({"success":"True","token":token,"user":db_user.output()})
                except Exception as err:
                    return f"err"
        except:
            return jsonify({"status":"Fail","message":"username or password incorrect"})
        
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

        token = generateToken(username)

        return jsonify({"success":"True","message":"account created successfully.","user":new_user.output(),"token":token})

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
    
    # get the user by id, this will be for populating the author of each event


@users_routes.route("/author/<author_id>", methods=["GET"])
def get_author_by_id(author_id):
    if request.method == "GET":
        try:
            found_user = Users.query.filter_by(id=author_id).first()
            user = found_user.output()

            return jsonify({"author":user["username"]})
        except Exception as err:
            print(err)
            return jsonify({"message":"something went wrong fetching the author username"})

    
    
    
    
    
    
    
      
