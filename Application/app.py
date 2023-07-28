from flask import Flask, render_template, url_for
from testing.testing import Message, Stats, StatItem

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

@app.route("/get/upgrades/")
def get_upgrades():
    stats = load_stats()
    upgradables = load_upgrades()
    print(upgradables)
    return render_template("upgradeWindowTemplate.html", stats=stats, stat_items=upgradables)

def load_messages():
    with open("./testing/chatTest.txt") as fp:
        lines = fp.readlines()

    messages = []
    for line in lines:
        data = line.split(" ")
        messages.append(Message(data[0], data[1], " ".join(data[2:])))

    return messages

def load_stats():
    with open("./testing/statTest.txt") as fp:
        statline = fp.read()

    args = statline.split(" ")
    stats = Stats(*args)
    return stats

def load_upgrades():
    with open("./testing/upgradeTest.txt") as fp:
        stats = [StatItem(*line.strip().split(" ")) for line in fp.readlines()]
    return stats
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=20000, debug=True)