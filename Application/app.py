# External imports
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_socketio import SocketIO, emit
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from random import choice
from json import loads
from dotenv import dotenv_values

# Testing
# from testing.OldClass.testing import Message, Stats, StatItem, Item, ShopItem
# from testing.OldClass.testing import *
# from modelTesting import *

# Application
from models.models import *
from models.extensions import db
from models.objects.objects import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SECRET_KEY'] = dotenv_values(".env")["SECRET"]

db.init_app(app)
socketio: SocketIO = SocketIO(app)

login_manager = LoginManager()
login_manager.login_view = "/auth/login/"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id:int):
    print(User.query.get(user_id))
    return User.query.get(int(user_id))

@app.route("/")
@login_required
def index():
    return render_template("index.html", name=current_user.name)

@app.route("/auth/<string:mode>/")
def login_signup(mode:str):
    if mode not in ["login", "register"]:
        mode = "register"
    return render_template("login.html", mode=mode.title())

@app.route("/auth/login/", methods=["POST"])
def login():
    name = request.form.get("name")
    password = request.form.get('password')
    remember = request.form.get("remember")

    user:User = db.session.execute(db.select(User).filter_by(name=name)).first()

    if not user or not check_password_hash(user[0].password, password):
        flash("Please check your login details and try again.", "is-danger")
        return redirect("/auth/login/")
    
    if login_user(user[0], remember=remember):
        flash("Logged in! Welcome " + name, "is-success")
    else:
        flash("You could not be logged in.", "is-info")
        return redirect("/auth/login/")
    return redirect("/")

@app.route("/auth/register/", methods=["POST"])
def register():
    name = request.form.get("name")
    password = request.form.get("password")
    password2 = request.form.get("password2")

    if len(name) < 2 or len(password) < 5:
        flash("Name and / or Password is too short.", "is-info")
        return redirect("/auth/register/")

    user = db.session.execute(db.select(User).filter_by(name=name)).first()
    if user:
        flash("This name is already taken.", "is-warning")
        return redirect("/auth/register/")
    
    if password != password2:
        flash("Your passwords do not match", "is-warning")
        return redirect("/auth/register/")

    
    new_user = User(name=name, password=generate_password_hash(password, method="scrypt"))
    db.session.add(new_user)
    db.session.commit()

    fighter = Fighter.create_new_fighter(id_=new_user.id, name=new_user.name)
    db.session.add(fighter)
    db.session.commit()

    stats = Stats.create_stats(id_=new_user.id)
    db.session.add(stats)
    db.session.commit()


    flash("Your account has been successfully created.", "is-success")
    return redirect("/auth/login/")

@app.route("/auth/logout/")
@login_required
def logout():
    logout_user()
    flash("Logged out", "is-info")
    return redirect("/auth/login/")

# Getters
all_messages:[Message] = []

@app.route("/get/message/")
def get_message():
    if not all_messages: return "" 
    return all_messages.pop(0).get_html()

@app.route("/get/stats/")
@login_required
def get_profile():
    profile = get_fighter_from_user()
    return render_template("statWindowTemplate.html", stats=profile)

@app.route("/get/upgrades/")
@login_required
def get_upgrades():
    stats: Stats = get_fighter_from_user().stats
    upgradables = stats.get_upgrades_html()
    return render_template("upgradeWindowTemplate.html", stats=stats, stat_items=upgradables)

@app.route("/get/inventory/")
@login_required
def get_inventory():
    player = get_fighter_from_user()
    stats = player.stats
    tier, pcoins = stats.tier, stats.pcoins
    items = load_inventory(player.inventory)
    return render_template("inventoryWindowTemplate.html", items=items, tier=tier, pcoins=pcoins)

@app.route("/get/shop/")
@app.route("/get/shop/<string:type_>/")
@login_required
def get_shop(type_=""):
    stats = get_fighter_from_user().stats
    tier, pcoins, level = stats.tier, stats.pcoins, stats.level
    items = load_shop() if not type_ else load_shop(type_)

    page = "shopWindowTemplate.html" if not type_ else "shopItemsTemplate.html"

    return render_template(page, tier=tier, pcoins=pcoins, level=level, items=items)

@app.route("/get/enemy/<int:enemy_id>/")
@login_required
def get_enemy(enemy_id:int):
    if not enemy_id:
        return {"body": "No ID was provided."}
    
    enemy = db.session.execute(db.select(Enemy).filter_by(id=enemy_id)).first()
    if not enemy:
        return "No enemy with that ID exists."
    return render_template("statWindowTemplate.html", stats=enemy[0])

@app.route("/get/job/")
@login_required
def get_job():
    jobs = db.session.execute(db.select(Job).filter_by(tier=choice([1, 2, 3, 4]))).fetchall()
    job:Job = choice(jobs)[0]

    if job:
        return job.get_response()
    return {"RESPONSE": None, "ERROR": "No jobs could be found currently."}

# Getting buttons
@app.route("/get/buttons/<string:type_>/")
def get_buttons(type_:str):
    return render_template("actionButtons.html", type=type_)

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
    
    player:Character = get_fighter_from_user()
    
    all_messages.append(Message(player.id, sender, sender_name, content))
    emit("messageMe", {"data": None})
    return {"Status": "Success"}

@app.route("/add/job/", methods=["POST"])
def add_job():
    data = loads(request.json)
    job = Job(**data)

    db.session.add(job)
    db.session.commit()

    return {"Status": "Success"}

# Socket Stuffies
@socketio.on("message")
def add_message_socket(data):
    data = loads(data)
    sender = data.get("sender", None)
    sender_name = data.get("sender_name", None)
    content = data.get("content", None)

    if not all([sender, sender_name, content]):
        return {"error": "Insufficient Data"}
    
    player:Character = get_fighter_from_user()
    
    message = Message(player.id, sender, sender_name, content)

    emit("message", {"body": message.get_html()})


@socketio.on("introduce")
def introduce(message):
    m = Message(1, "system", "system", "Welcome to Fight Parade")
    emit('message', {"body": m.get_html()})
    emit("response", {"data": "We're glad to have you here!"})


# Helpers!
def get_fighter_from_user() -> Fighter:
    """Retrieves the fighter object from the logged in user.
    
    Returns:
        Fighter"""
    
    return db.session.execute(db.select(Fighter).filter_by(id=current_user.id)).first()[0]

def load_inventory(item_str:str) -> [Item]:
    """Loads the player's inventory into actual Item objects
    
    Returns:
        List of Item"""
    
    if not item_str: return []
    item_ids = [int(item_id.strip()) for item_id in item_str.rstrip(',').split(",")]

    items = [db.session.execute(db.select(Item).filter_by(id=item_id)).first() for item_id in item_ids]

    return [item[0] for item in items]

def load_shop(item_type="", tier=None) -> "[BaseItem] | None":
    """Loads all items from the database matching the specified type and tier.
    
    Args:
        item_type (str): The type of item to find.
        tier (int): The tier of items to show.
        
    Returns:
        List of items"""
    
    if item_type:
        if item_type == "skill":
            abils = db.session.execute(db.select(BaseItem).filter_by(item_type="ability")).fetchall()
            passives = db.session.execute(db.select(BaseItem).filter_by(item_type='passive')).fetchall()
            items = [*abils, *passives]
        else:
            items = db.session.execute(db.select(BaseItem).filter_by(item_type=item_type.lower())).fetchall()
    else:
        items = db.session.execute(db.select(BaseItem)).fetchall()
    
    if items: 
        if not tier:
            user_tier = get_fighter_from_user().stats.tier
            return [item[0] for item in items if item[0].tier == user_tier]
        elif tier == -1:
            return [item[0] for item in items]
        else:
            return [item[0] for item in items if item[0].tier == tier]
        
    else: return None

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=20000, debug=True)