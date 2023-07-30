"""File to store the item model and information."""

class BaseItem:
    """Base class for all Items (Item, Gear and Skills)"""

    def __init__(self, name:str, id_:int, description:str, tooltip:str, effect:dict, cost:int, tier:int, reborn:int):
        self.name = name 
        self.id = id_
        self.description = description
        self.tooltip = tooltip 
        self.effect = effect
        self.cost = cost
        self.tier = tier 
        self.reborn = reborn

class Item(BaseItem):
    """Class used to rerpresent consumable items"""

    def __init__(self, name: str, id_: int, description: str, tooltip: str, effect: dict, cost:int, tier: int, duration):
        super().__init__(name, id_, description, tooltip, effect, tier, 0)
        self.duration = duration


