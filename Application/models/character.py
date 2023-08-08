"""File to store the character model and information."""
from .extensions import db

class Character(db.Model):
    """This is the base class that represents Characters."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    stats_id = db.Column(db.Integer, db.ForeignKey('stats.id'))
    weapon_id = db.Column(db.Integer, db.ForeignKey("weapon.id"))
    armour_id = db.Column(db.Integer, db.ForeignKey("armour.id"))
    ability_id = db.Column(db.Integer, db.ForeignKey("ability.id"))
    passive_id = db.Column(db.Integer, db.ForeignKey("passive.id"))
    stats = db.relationship("Stats", foreign_keys=[stats_id], backref='character')
    weapon = db.relationship("Weapon", foreign_keys=[weapon_id], backref='character', lazy=True)
    armour = db.relationship("Armour", foreign_keys=[armour_id], backref='character', lazy=True)
    ability = db.relationship("Ability", foreign_keys=[ability_id], backref='character', lazy=True)
    passive = db.relationship("Passive", foreign_keys=[passive_id], backref='character', lazy=True)

    def get_str(self):
        return f"""<div id="profileData">
  <div id="profileHeader" class="columns">
    <div id="headerImage" class="column">
      <img
        src="https://avatars.dicebear.com/api/human/{self.name}.svg"
        alt=""
        height="80px"
        width="80px"
      />
    </div>
    <div id="headerData" class="column is-three-quarters">
      <p>Name: {self.name}</p>
      <progress
        class="progress is-primary"
        value="{self.stats.exp}"
        max="{self.stats.max_exp}"
      >
        {round((self.stats.exp / self.stats.max_exp) * 100, 2)}%
      </progress>
      <div id="levelInfo">
        <p>Exp: { self.stats.exp }/{ self.stats.max_exp }</p>
        <span>Level { self.stats.level }</span>
      </div>
    </div>
  </div>
  <hr />
  <div id="profileBody" class="columns">
    <div id="profileColumn1" class="column">
      <p>Health: { self.stats.health } / { self.stats.base_health }</p>
      <p>Power: { self.stats.power }</p>
      <p>Crit Chance: { self.stats.crit_chance }%</p>
      <p>Ability: { getattr(self.ability, 'name', None)}</p>
    </div>
    <div id="profileColumn2" class="column">
      <p>Tier { self.stats.tier }</p>
      <p>Defense: { self.stats.defense }</p>
      <p>Heal Chance: { self.stats.heal_chance }%</p>
      <p>Passive: { getattr(self.passive, 'name', None)}</p>
    </div>
  </div>
</div>"""


class Fighter(Character):
    """This is the Player class that players will use to navigate through the game"""

    id = db.Column(db.Integer, db.ForeignKey('character.id'), primary_key=True)
    inventory = db.Column(db.String(100))

class Enemy(Character):
    """THis is the Enemy class that will represent foes in the game"""

    id = db.Column(db.Integer, db.ForeignKey("character.id"), primary_key=True)
    entry_message = db.Column(db.String(200))
    attack_message = db.Column(db.String(200))
    item = db.Column(db.String(10))
