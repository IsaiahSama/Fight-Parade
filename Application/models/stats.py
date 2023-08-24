"""This class is responsible for managing the stats for Players and enemies"""

from .extensions import db 
from .objects.tier import get_tier
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

    @staticmethod
    def create_stats(id_:int = id):
        return Stats(id=id_, level=1, pcoins=50, exp=0, max_exp=35, tier=1, health=50, base_health=50, power=5, base_power=5, defense=0, base_defense=0, crit_chance=3, base_crit=3, heal_chance=5, base_heal=5)

    def get_upgrades_dict(self) -> dict:
        """Methods used to get the upgrades in the form of a dictionary.
        
        Returns:
            dicts"""
        
        upgrades = {
            "health": {
                "incr": 5,
                "price": 35
            },
            "power": {
                "incr": 2,
                "price": 50
            },
            "defense": {
                "incr": 1,
                "price": 40
            }, 
            "crit": {
                "incr": 1,
                "price": 80
            },
            "heal": {
                "incr": 1,
                "price": 70
            }
        }
        
        return upgrades

    def get_upgrades_html(self) -> str:
        """Gets the HTML for the upgrades.
        
        Returns:
            str"""
        
        upgrades = self.get_upgrades_dict()
        
        stats = ["health", "power", "defense", "crit", "heal"]
        tier = get_tier(self.tier)

        html = ""
        for stat in stats:
            title = stat.title() if stat in stats[:3] else "base_" + stat
            statement = """
            <div class="upgradeStatCard card">
                <p class="card-header-title is-centered">
            {title}: {base_stat} / {max_stat}
                </p>
                <div class="card-footer">
                <p class="card-footer-item">Increase by: {incr}</p>
                <p class="card-footer-item">Price: {price}₱</p>
                </div>
            </div>""".format(title=title, base_stat=eval(f"self.base_{stat}"), max_stat=eval(f"tier.max_{stat}"), incr=upgrades[stat]['incr'], price=upgrades[stat]['price'])

            html += statement

        return html

