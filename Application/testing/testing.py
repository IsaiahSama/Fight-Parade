"""This is a file where classes made for testing will be placed."""

class Message:
    def __init__(self, sender, sender_name, content):
        self.sender = sender
        self.sender_name = sender_name
        self.content = content

class Stats:
    def __init__(self, name, level, exp, max_exp, health, max_health, tier, power, defense, crit_chance, heal_chance, ability, passive ):
        self.name = name
        self.level = level 
        self.exp = exp 
        self.max_exp = max_exp
        self.per_exp = (int(exp) / int(max_exp)) * 100
        self.health = health 
        self.max_health = max_health
        self.tier = tier 
        self.power = power 
        self.defense = defense 
        self.crit_chance = crit_chance
        self.heal_chance = heal_chance 
        self.ability = ability
        self.passive = passive
        self.pcoins = 99999999

class StatItem:
    def __init__(self, name, current_max, cap, incr, price):
        self.name = name
        self.current_max = current_max
        self.cap = cap
        self.incr = incr
        self.price = price.strip()

class Item:
    def __init__(self, id_, name, tier, amount="N/A"):
        self.id = id_ 
        self.name = name 
        self.tier = tier
        self.amount = amount
        self.img = "https://api.dicebear.com/6.x/icons/svg?seed="+name

    def __str__(self):
        return f"""
        <div class="itemCard card">
            <div class="card-image">
                <center>
                    <img src="{ self.img }" alt="" width="50px" height="50px" />
                </center>
            </div>
            <div class="card-header-title is-centered">{ self.name }</div>
            <div class="card-footer">
                <p class="card-footer-item">Amount: { self.amount }</p>
                <p class="card-footer-item">ID: { self.id }</p>
                <p class="card-footer-item">Tier: { self.tier }</p>
            </div>
        </div>"""

class ShopItem:
    def __init__(self, id_, name, tier, price, type_):
        self.id = id_
        self.name = name 
        self.tier = tier 
        self.price = price
        self.type = type_
        self.img = "https://api.dicebear.com/6.x/icons/svg?seed="+name