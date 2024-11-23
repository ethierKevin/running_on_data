from flask import Blueprint, jsonify, request
from extensions import db
from models import User,db,Activity
from csv_parser import parse_csv

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



@main_blueprint.route('/upload_csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not file.filename.endswith('.csv'):
        return jsonify({'error': 'Invalid file type, only .csv allowed'}), 400

    try:
        data = parse_csv(file.stream)  # Use the utility function
        for entry in data:
            activity = Activity(
                date=entry['date'], 
                distance=float(entry['distance']), 
                time=entry['time']
            )
            db.session.add(activity)

        db.session.commit()
        return jsonify({'message': 'CSV data successfully uploaded and saved'}), 201
    except Exception as e:
        return jsonify({'error': f'Failed to process CSV: {str(e)}'}), 500
