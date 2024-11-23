from extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    activities = db.relationship('Activity', backref='user', lazy=True)
    
    def to_dict(self):
        return {
        "id": self.id,
        "username": self.username,
        "email": self.email
    }

class Activity(db.Model):   
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    distance = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    pace = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    metrics = db.relationship('Metrics', backref='activity', uselist=False)

    def __repr__(self):
        return f'<Activity {self.date} - {self.distance} miles / {self.duration} minutes and pace was {self.pace}>'

class Metrics(db.Model):
    __tablename__ = 'metrics'
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'), nullable=False)
    heart_rate = db.Column(db.Integer)
    calories_burned = db.Column(db.Float)
    elevation_gain = db.Column(db.Float)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
