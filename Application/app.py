from flask import Flask, render_template, url_for

app = Flask(__name__)

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

class Message:
    def __init__(self, sender, sender_name, content):
        self.sender = sender
        self.sender_name = sender_name
        self.content = content

def load_messages():
    with open("chatTest.txt") as fp:
        lines = fp.readlines()

    messages = []
    for line in lines:
        data = line.split(" ")
        messages.append(Message(data[0], data[1], " ".join(data[2:])))

    return messages

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

def load_stats():
    with open("statTest.txt") as fp:
        statline = fp.read()

    args = statline.split(" ")
    stats = Stats(*args)
    return stats

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=20000, debug=True)