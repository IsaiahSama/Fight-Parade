"""File to store the character model and information."""

class Character:
    """This is the base class that represents Characters."""
   
    def __init__(self, name:str, id_:int, level:int, health:int, power:int, heal_chance:int, crit_chance:int, weapon:str, armour:str, ability:str, passive:str, tier:int):
        self.name = name
        self.id = id_ 
        self.level = level
        self.health = health 
        self.power = power 
        self.heal_chance = heal_chance
        self.crit_chancne = crit_chance
        self.weapon = weapon 
        self.armour = armour 
        self.ability = ability
        self.passive = passive 
        self.tier = tier 

class Fighter(Character):
    """This is the Player class that players will use to navigate through the game"""

    def __init__(self, name, id_, level=0, health=50, power=10, heal_chance=5, crit_chance=5, weapon="0000", armour="0000", ability="0000", passive="0000", tier=1, paradians=0, inventory=[]):
        super().__init__(name, id_, level, health, power, heal_chance, crit_chance, weapon, armour, ability, passive, tier)
        self.paradians = paradians
        self.inventory = inventory

class Enemy(Character):
    """THis is the Enemy class that will represent foes in the game"""

    def __init__(self, name, id_, level=0, health=50, power=10, heal_chance=5, crit_chance=5, weapon="0000", armour="0000", ability="0000", passive="0000", tier=1, entry_message:str="", attack_message:str="", xp_yield:int=0, coin_yield:int=0, item:str=""):
        super().__init__(name, id_, level, health, power, heal_chance, crit_chance, weapon, armour, ability, passive, tier)
        self.entry_message = entry_message
        self.attack_message = attack_message
        self.xp_yield = xp_yield
        self.coin_yield = coin_yield
        self.item = item