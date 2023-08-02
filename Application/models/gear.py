"""File to store the gear model and information."""
from item import BaseItem
from .extensions import db

class Weapon(BaseItem):
    """Represents a weapon."""
    id = db.Column(db.Integer, db.ForeignKey('BaseItem.id'), primary_key=True)

class Armour(BaseItem):
    """Represents Armour"""
    id = db.Column(db.Integer, db.ForeignKey('BaseItem.id'), primary_key=True)