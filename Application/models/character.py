"""File to store the character model and information."""
from .extensions import db

class Character(db.Model):
    """This is the base class that represents Characters."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    level = db.Column(db.Integer)
    health = db.Column(db.Integer)
    power = db.Column(db.Integer)
    heal_chance = db.Column(db.Integer)
    crit_chance = db.Column(db.Integer)
    weapon = db.relationship("Weapon", backref='character', lazy=True)
    armour = db.relationship("Armour", backref='character', lazy=True)
    ability = db.relationship("Ability", backref='character', lazy=True)
    passive = db.relationship("Passive", backref='character', lazy=True)
    tier = db.Column(db.Integer)


class Fighter(Character):
    """This is the Player class that players will use to navigate through the game"""

    id = db.Column(db.Integer, db.ForeignKey('character.id'), primary_key=True)
    paradians = db.Column(db.Integer)
    inventory = db.Column(db.String(100))

    # __mapper_args__ = {
    #     'polymorphic_identity': 'fighter',
    # }

class Enemy(Character):
    """THis is the Enemy class that will represent foes in the game"""

    id = db.Column(db.Integer, db.ForeignKey("character.id"), primary_key=True)
    entry_message = db.Column(db.String(200))
    attack_message = db.Column(db.String(200))
    xp_yield = db.Column(db.Integer)
    coin_yield = db.Column(db.Integer)
    item = db.Column(db.String(10))

    # __mapper_args__ = {
    #     'polymorphic_identity': 'enemy',
    # }
