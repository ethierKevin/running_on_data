from flask import Blueprint, jsonify
from extensions import db
from models import User

# init blueprint
main_blueprint = Blueprint('main', __name__)

# home
@main_blueprint.route('/')
def home():
    return jsonify(message="Running On Data API")

# dummy data entry for poc 
@main_blueprint.route("/populate_db")
def populate_db():
    try:
        dummy_users = [
            User(username="Eliud", email="eliud@example.com"),
            User(username="Kenenisa", email="kenenisa@example.com"),
            User(username="Jakob", email="jakob@example.com")
        ]
        db.session.add_all(dummy_users)
        db.session.commit()
        return jsonify({"message": "Database populated with dummy data!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

# test route to query db for dummy vals populated
@main_blueprint.route("/get_users", methods=["GET"])
def get_users():
    try:
        # select all from User table
        users = User.query.all()
        
        # convert to dict from user obj
        user_list = [user.to_dict() for user in users]
        
        # return sql output 
        return jsonify(user_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
