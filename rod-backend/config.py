import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://kevinethier:golfSKI*1984@localhost/running_on_data")
    SQLALCHEMY_TRACK_MODIFICATIONS = False