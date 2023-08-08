from flask import Flask, render_template, url_for, request
from testing.OldClass.testing import Message, Stats, StatItem, Item, ShopItem
from models.models import *
from models.extensions import db
from json import loads

from testing.OldClass.testing import *
from modelTesting import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

# Getters
@app.route("/get/chat/")
def get_chat():
    messages = load_messages()
    return render_template("chatBodyTemplate.html", messages=messages)

@app.route("/get/stats/")
def get_stats():
    stats = load_stats()
    return render_template("statWindowTemplate.html", stats=stats)

@app.route("/get/upgrades/")
def get_upgrades():
    stats = load_stats()
    upgradables = load_upgrades()
    return render_template("upgradeWindowTemplate.html", stats=stats, stat_items=upgradables)

@app.route("/get/inventory/")
def get_inventory():
    stats = load_stats()
    tier, pcoins = stats.tier, stats.paradians
    items = load_inventory()
    return render_template("inventoryWindowTemplate.html", items=items, tier=tier, pcoins=pcoins)

@app.route("/get/shop/")
@app.route("/get/shop/<string:type_>/")
def get_shop(type_=""):
    stats = load_stats()
    tier, pcoins, level = stats.tier, stats.paradians, stats.level
    items = load_items()

    if type_:
        items = list(filter(lambda x: x.type == type_, items))

    page = "shopWindowTemplate.html" if not type_ else "shopItemsTemplate.html"

    return render_template(page, tier=tier, pcoins=pcoins, level=level, items=items)

# Adding
@app.route("/add/user/", methods=["POST"])
def add_user():
    data = loads(request.json)
    fighter = Fighter(**data)
    db.session.add(fighter)
    db.session.commit()
    return {"Status": "success"}

@app.route("/add/enemy/", methods=["POST"])
def add_enemy():
    data = loads(request.json)
    enemy = Enemy(**data)
    db.session.add(enemy)
    db.session.commit()
    return {"Status": "success"}

@app.route("/add/weapon/", methods=["POST"])
def add_weapon():
    data = loads(request.json)
    weapon = Weapon(**data)
    db.session.add(weapon)
    db.session.commit()
    return {"Status": "success"}

@app.route("/add/armour/", methods=["POST"])
def add_armour():
    data = loads(request.json)
    armour = Armour(**data)
    db.session.add(armour)
    db.session.commit()
    return {"Status": "success"}

@app.route("/add/ability/", methods=["POST"])
def add_ability():
    data = loads(request.json)
    ability = Ability(**data)
    db.session.add(ability)
    db.session.commit()
    return {"Status": "success"}

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=20000, debug=True)