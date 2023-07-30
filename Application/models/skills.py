"""File to store the skill model and information."""

from item import BaseItem

class Ability(BaseItem):
    """Represents an Ability"""

    def __init__(self, name: str, id_: int, description: str, tooltip: str, effect: dict, cost:int, tier: int, reborn: int, chant:str, cooldown:int):
        super().__init__(name, id_, description, tooltip, effect, cost, tier, reborn)
        self.chant = chant 
        self.cooldown = cooldown

class Passive(Ability):
    pass