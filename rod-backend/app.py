from flask import Flask,jsonify
from config import Config
from extensions import db, migrate
from models import User, Activity, Metrics
from flask_cors import CORS
from routes import main_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['WTF_CSRF_ENABLED'] = False

    # enable CORs for cross site to port 3000
    CORS(app, resources={r"/upload_csv": {"origins": "http://localhost:3000"}})

    # CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
    # CORS(app, resources={r"/*": {"origins": "*"}})



    # ext initilaize
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(main_blueprint)

    @app.after_request
    def after_request(response):
        print("Adding CORS headers to the response")  # Debug log
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS,PUT,DELETE'
        return response

    # test
    @app.route("/test_db")
    def test_db():
        try:
            # db connect test
            users = User.query.all()
            return jsonify([user.to_dict() for user in users])  
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    return app