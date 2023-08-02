"""This serves as the source point for the Flask Application."""
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
# db.init_app(app)