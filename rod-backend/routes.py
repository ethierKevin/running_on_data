from flask import Blueprint, jsonify, request,Flask
from extensions import db
from models import User,db,Activity
import csv
from flask_cors import CORS


# init blueprint
main_blueprint = Blueprint('main', __name__)

# home
@main_blueprint.route('/')
def home():
    return jsonify(message="Running On Data API")

# dummy data entry for poc 
@main_blueprint.route("/populate_db")

def parse_csv(file_stream):
    data = []
    csv_reader = csv.DictReader(file_stream)
    for row in csv_reader:
        data.append(row)
    return data

# test requests are getting to backend
@main_blueprint.before_request
def log_request_info():
    print("Incoming request method:", request.method)
    print("Incoming request path:", request.path)
    print("Incoming request headers:", request.headers)


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
    print("Request headers:", request.headers)
    print("Request origin:", request.headers.get('Origin'))
    print("Request files:", request.files)

    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not file.filename.endswith('.csv'):
        return jsonify({'error': 'Invalid file type, only .csv allowed'}), 400

    
    try:
        # decode from binary? 
        decoded_file = file.stream.read().decode('utf-8')
        csv_reader = csv.reader(decoded_file.splitlines())

        #process csv file
        rows = [row for row in csv_reader]
        print(f"Processed rows: {rows}")

        return jsonify({'message': f"File {file.filename} uploaded successfully!", 'rows': rows}), 200

    except Exception as e:
        print(f"Error processing CSV: {e}")
        return jsonify({'error': f"Failed to process CSV: {e}"}), 500

