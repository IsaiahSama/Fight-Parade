"""This serves as the source point for the Flask Application."""
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()