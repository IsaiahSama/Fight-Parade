"""This class represents the Job model."""
from .extensions import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120))
    tier = db.Column(db.Integer)
