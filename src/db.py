from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app.config["SQLALCHEMY_DATABASE_URL"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
