"""File to store the character model and information."""
from .extensions import db

class Character(db.Model):
    """This is the base class that represents Characters."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    level = db.Column(db.Integer)
    exp = db.Column(db.Integer)
    max_exp = db.Column(db.Integer)
    health = db.Column(db.Integer)
    power = db.Column(db.Integer)
    heal_chance = db.Column(db.Integer)
    crit_chance = db.Column(db.Integer)
    weapon_id = db.Column(db.Integer, db.ForeignKey("weapon.id"))
    armour_id = db.Column(db.Integer, db.ForeignKey("armour.id"))
    ability_id = db.Column(db.Integer, db.ForeignKey("ability.id"))
    passive_id = db.Column(db.Integer, db.ForeignKey("passive.id"))
    tier = db.Column(db.Integer)
    weapon = db.relationship("Weapon", foreign_keys=[weapon_id], backref='character', lazy=True)
    armour = db.relationship("Armour", foreign_keys=[armour_id], backref='character', lazy=True)
    ability = db.relationship("Ability", foreign_keys=[ability_id], backref='character', lazy=True)
    passive = db.relationship("Passive", foreign_keys=[passive_id], backref='character', lazy=True)




class Fighter(Character):
    """This is the Player class that players will use to navigate through the game"""

    id = db.Column(db.Integer, db.ForeignKey('character.id'), primary_key=True)
    paradians = db.Column(db.Integer)
    inventory = db.Column(db.String(100))

class Enemy(Character):
    """THis is the Enemy class that will represent foes in the game"""

    id = db.Column(db.Integer, db.ForeignKey("character.id"), primary_key=True)
    entry_message = db.Column(db.String(200))
    attack_message = db.Column(db.String(200))
    xp_yield = db.Column(db.Integer)
    coin_yield = db.Column(db.Integer)
    item = db.Column(db.String(10))
