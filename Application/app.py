# Key imports
from flask import Flask, render_template, url_for, request
from flask_socketio import SocketIO, emit
from random import choice
from json import loads
from dotenv import dotenv_values

# Testing
from testing.OldClass.testing import Message, Stats, StatItem, Item, ShopItem
from testing.OldClass.testing import *
from modelTesting import *

# Application
from models.models import *
from models.extensions import db
from objects.objects import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SECRET_KEY'] = dotenv_values(".env")["SECRET"]

db.init_app(app)
socketio: SocketIO = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")

# Getters
all_messages:[Message] = [Message(1, "system", "system", "Welcome to Fight Parade")]

@app.route("/get/message/")
def get_message():
    if not all_messages: return "" 
    return all_messages.pop(0).get_html()

@app.route("/get/stats/")
def get_profile():
    profile = load_stats()
    return render_template("statWindowTemplate.html", stats=profile)

@app.route("/get/upgrades/")
def get_upgrades():
    stats = load_stats().stats
    upgradables = load_upgrades()
    return render_template("upgradeWindowTemplate.html", stats=stats, stat_items=upgradables)

@app.route("/get/inventory/")
def get_inventory():
    player = load_stats()
    stats = player.stats
    tier, pcoins = stats.tier, stats.pcoins
    items = load_inventory(player.inventory)
    return render_template("inventoryWindowTemplate.html", items=items, tier=tier, pcoins=pcoins)

@app.route("/get/shop/")
@app.route("/get/shop/<string:type_>/")
def get_shop(type_=""):
    stats = load_stats().stats
    tier, pcoins, level = stats.tier, stats.pcoins, stats.level
    items = load_items() if not type_ else load_items(type_)

    page = "shopWindowTemplate.html" if not type_ else "shopItemsTemplate.html"

    return render_template(page, tier=tier, pcoins=pcoins, level=level, items=items)

@app.route("/get/enemy/")
def get_enemy():
    enemy = load_enemy()
    return render_template("statWindowTemplate.html", stats=enemy)

@app.route("/get/job/")
def get_job():
    jobs = db.session.execute(db.select(Job).filter_by(tier=choice([1, 2, 3, 4]))).fetchall()
    job:Job = choice(jobs)[0]

    if job:
        return {"RESPONSE": job.description}
    return {"RESPONSE": None}

# Adding
@app.route("/add/user/", methods=["POST"])
def add_user():
    data = loads(request.json)
    fighter = Fighter(**data)
    db.session.add(fighter)
    db.session.commit()
    return {"Status": "success"}

@app.route("/add/stats/", methods=["POST"])
def add_stats():
    data = loads(request.json)
    stats = Stats(**data)
    db.session.add(stats)
    db.session.commit()
    return {"Status": "success"}

@app.route("/add/enemy/", methods=["POST"])
def add_enemy():
    data = loads(request.json)
    enemy = Enemy(**data)
    db.session.add(enemy)
    db.session.commit()
    return {"Status": "success"}

item_types = {
    "ability": Ability,
    "passive": Passive,
    "item": Item,
    "weapon": Weapon,
    "armour": Armour
}

img_base_url = "https://api.dicebear.com/6.x/icons/svg?seed={0}"

@app.route('/add/item/', methods=["POST"])
def add_item():
    data:BaseItem = loads(request.json)
    item_type = data["item_type"]
    data["img_url"] = img_base_url.format(data['name'])
    item = item_types[item_type](**data)
    db.session.add(item)
    db.session.commit()

    return {"Status": "success"}

@app.route("/add/message/", methods=["POST"])
def add_message():
    data = request.json
    sender = data.get("sender", None)
    sender_name = data.get("sender_name", None)
    content = data.get("content", None)

    if not all([sender, sender_name, content]):
        return {"error": "Insufficient Data"}
    
    player:Character = load_stats()
    
    all_messages.append(Message(player.id, sender, sender_name, content))
    return {"Status": "Success"}

@app.route("/add/job/", methods=["POST"])
def add_job():
    data = loads(request.json)
    job = Job(**data)

    db.session.add(job)
    db.session.commit()

    return {"Status": "Success"}

# Socket Stuffies

@socketio.on("connect")
def test_connect(message):
    emit("response", {"data": "Succeessfully connected"})

@socketio.on("introduce")
def introduce(message):
    print("Someone's introducing themselves.")
    print(message['data'])
    emit("response", {"data": "We're glad to have you here!"})

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=20000, debug=True)