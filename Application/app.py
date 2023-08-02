from flask import Flask, render_template, url_for, request
from testing.OldClass.testing import Message, Stats, StatItem, Item, ShopItem
from models.models import *
from models.extensions import db
from modelTesting import create_models
from json import loads

from testing.OldClass.testing import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

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
    tier, pcoins = stats.tier, stats.pcoins
    items = load_inventory()
    return render_template("inventoryWindowTemplate.html", items=items, tier=tier, pcoins=pcoins)

@app.route("/get/shop/")
@app.route("/get/shop/<string:type_>/")
def get_shop(type_=""):
    stats = load_stats()
    tier, pcoins, level = stats.tier, stats.pcoins, stats.level
    items = load_items()

    if type_:
        items = list(filter(lambda x: x.type == type_, items))

    page = "shopWindowTemplate.html" if not type_ else "shopItemsTemplate.html"

    return render_template(page, tier=tier, pcoins=pcoins, level=level, items=items)

@app.route("/add/user/", methods=["POST"])
def add_user():
    data = loads(request.json)
    fighter = Fighter(
        id=data['id'],
        name=data['name'],
        level=data['level'],
        health=data['health'],
        power=data['power'],
        heal_chance=data['heal'],
        crit_chance=data['crit'],
        weapon_id=data['weapon'],
        armour_id=data['armour'],
        ability_id=data['ability'],
        passive_id=data['passive'],
        tier=data['tier'],
        paradians=data['paradians'],
        inventory=data['inventory']
    )
    db.session.add(fighter)
    db.session.commit()
    return {"Status": "success"}

@app.route("/add/enemy/", methods=["POST"])
def add_enemy():
    pass

@app.route("/add/weapon/", methods=["POST"])
def add_weapon():
    pass

@app.route("/add/armour/", methods=["POST"])
def add_armour():
    pass

@app.route("/add/ability/", methods=["POST"])
def add_ability():
    pass

def create_new_character(**kwargs):
    character = Character(**kwargs) 
    db.session.add(character)
    db.session.commit()

def create_new_item_base(**kwargs):
    base_item = BaseItem(**kwargs)
    db.session.add(base_item)
    db.session.commit()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=20000, debug=True)