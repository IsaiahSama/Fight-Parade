"""File to store the item model and information."""
from .extensions import db 

class BaseItem(db.Model):
    """Base class for all Items (Item, Gear and Skills)"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(70))
    tooltip = db.Column(db.String(50))
    effect = db.Column(db.String(150))
    cost = db.Column(db.Integer)
    tier = db.Column(db.Integer)
    reborn = db.Column(db.Integer)

class Item(BaseItem):
    """Class used to rerpresent consumable items"""

    id = db.Column(db.Integer, db.ForeignKey('base_item.id'), primary_key=True)
    duration = db.Column(db.Integer)

