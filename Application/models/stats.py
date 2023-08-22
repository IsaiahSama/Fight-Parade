"""This class is responsible for managing the stats for Players and enemies"""

from .extensions import db 
import sqlalchemy as sa

class Stats(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    level = sa.Column(sa.Integer)
    pcoins = sa.Column(sa.Integer)
    exp = sa.Column(sa.Integer)
    max_exp = sa.Column(sa.Integer)
    tier = sa.Column(sa.Integer)
    health = sa.Column(sa.Integer)
    base_health = sa.Column(sa.Integer)
    power = sa.Column(sa.Integer)
    base_power = sa.Column(sa.Integer)
    defense = sa.Column(sa.Integer)
    base_defense = sa.Column(sa.Integer)
    crit_chance = sa.Column(sa.Integer)
    base_crit = sa.Column(sa.Integer)
    heal_chance = sa.Column(sa.Integer)
    base_heal = sa.Column(sa.Integer)



