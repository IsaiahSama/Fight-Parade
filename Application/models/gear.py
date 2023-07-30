"""File to store the gear model and information."""
from item import BaseItem

class Weapon(BaseItem):
    """Represents a weapon."""

    def __init__(self, name: str, id_: int, description: str, tooltip: str, effect: dict, cost:int, tier: int, reborn:int):
        super().__init__(name, id_, description, tooltip, effect, cost, tier, reborn)

class Armour(BaseItem):
    """Represents Armour"""

    def __init__(self, name: str, id_: int, description: str, tooltip: str, effect: dict, cost:int, tier: int, reborn: int):
        super().__init__(name, id_, description, tooltip, effect, cost, tier, reborn)
