"""This class is used to represent the tiers for characters"""

class Tier:
    def __init__(self, max_level:int, max_health:int, max_power:int, max_defense:int, max_crit:int, max_heal:int):
        self.max_level = max_level
        self.max_health = max_health
        self.max_power = max_power
        self.max_defense = max_defense
        self.max_crit = max_crit 
        self.max_heal = max_heal


tier1 = Tier(50, 100, 20, 10, 5, 10)
tier2 = Tier(100, 200, 40, 20, 7, 12)
tier3 = Tier(200, 400, 80, 40, 10, 15)
tier4 = Tier(300, 800, 160, 80, 15, 18)
# Negative values means that these are minimums instead of maximums.
tier5 = Tier(-300, 1500, 300, 150, 20, 20)
tier6 = Tier(-300, -1000, -500, -250, -25, -25)

tiers = [tier1, tier2, tier3, tier4, tier5, tier6]