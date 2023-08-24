"""This model represents the user. Not the character."""
from .extensions import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    """This model represents a User Account."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(30))
    fighter = db.relationship("Fighter", backref="user", lazy=True)