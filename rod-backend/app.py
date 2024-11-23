from flask import Flask,jsonify
from config import Config
from extensions import db, migrate
from models import User, Activity, Metrics
from flask_cors import CORS
from routes import main_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # ext initilaize
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main_blueprint)

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