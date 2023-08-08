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
    defense = db.Column(db.Integer)
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

    def __str__(self):
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
        value="{self.exp}"
        max="{self.max_exp}"
      >
        {round((self.exp / self.max_exp) * 100, 2)}%
      </progress>
      <div id="levelInfo">
        <p>Exp: { self.exp }/{ self.max_exp }</p>
        <span>Level { self.level }</span>
      </div>
    </div>
  </div>
  <hr />
  <div id="profileBody" class="columns">
    <div id="profileColumn1" class="column">
      <p>Health: { self.health } / { self.health }</p>
      <p>Power: { self.power }</p>
      <p>Crit Chance: { self.crit_chance }%</p>
      <p>Ability: { getattr(self.ability, 'name', None)}</p>
    </div>
    <div id="profileColumn2" class="column">
      <p>Tier { self.tier }</p>
      <p>Defense: { self.defense }</p>
      <p>Heal Chance: { self.heal_chance }%</p>
      <p>Passive: { getattr(self.passive, 'name', None)}</p>
    </div>
  </div>
</div>"""


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
