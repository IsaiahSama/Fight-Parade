"""File to store the skill model and information."""

from item import BaseItem
from .extensions import db

class Ability(BaseItem):
    """Represents an Ability"""
    id = db.Column(db.Integer, db.ForeignKey('BaseItem.id'), primary_key=True)
    chant = db.Column(db.String(60))
    cooldown = db.Column(db.Integer)

class Passive(Ability):
    id = db.Column(db.Integer, db.ForeignKey('BaseItem.id'), primary_key=True)

    