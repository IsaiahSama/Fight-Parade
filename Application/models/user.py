"""This model represents the user. Not the character."""
from .extensions import db

class User(db.Model):
    """This model represents a User Account."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    password = db.Column(db.String(30))
    fighter = db.relationship("Fighter", backref="user", lazy=True)