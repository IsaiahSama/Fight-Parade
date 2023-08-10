"""In this file, we will test creating models!"""
from requests import post
from json import dumps
from models.extensions import db
from models.models import *

base = "./testing/Model/"
URL = "http://127.0.0.1:20000/add/"

def readlines(filename:str):
    with open(base+filename+".txt") as fp:
        lines = fp.readlines()

    return [line.strip() for line in lines]

def get_info(filename):
    lines = readlines(filename)
    fields = lines[0].split(" ")
    data = []

    for line in lines[1:]:
        l = line.split(" ")
        datum = {}
        for i in range(len(fields)):
            target: str = l[i]
            if "_" in target: target = target.replace("_", " ")
            if target.isnumeric(): target = int(target)
            if target in [-1, "-1"]: target = None

            datum[fields[i]] = target 
        data.append(datum)
    return data

def make_request(endpoint:str, items:list):
    for item in items:
        try:
            resp = post(URL+endpoint+"/", json=dumps(item))
            resp.raise_for_status()
            print(resp.json())
        except:
            print("An error occurred for ", item)


def create_models():
    # Getting the info
    fighters = get_info("fighters")
    enemies = get_info('enemies')
    stats = get_info("stats")
    items = get_info("items")
    weapons = get_info("weapons")
    armours = get_info("armours")
    abilities = get_info("abilities")
    passives  = get_info("passives")

    # Making the requests to update for fighter
    make_request("user", fighters)
    make_request('enemy', enemies)
    make_request('stats', stats)
    make_request("item", items)
    make_request("item", weapons)
    make_request("item", armours)
    make_request("item", abilities)
    make_request('item', passives)

def load_stats() -> Fighter:
    stats = db.session.execute(db.select(Fighter)).fetchone()
    
    if stats:
        return stats[0]
    else: 
        return None
    
def load_items(item_type="") -> BaseItem | None:
    if item_type:
        if item_type == "skill":
            abils = db.session.execute(db.select(BaseItem).filter_by(item_type="ability")).fetchall()
            passis = db.session.execute(db.select(BaseItem).filter_by(item_type='passive')).fetchall()
            items = [*abils, *passis]
        else:
            items = db.session.execute(db.select(BaseItem).filter_by(item_type=item_type.lower())).fetchall()
    else:
        items = db.session.execute(db.select(BaseItem)).fetchall()

    if items: return [item[0] for item in items]
    else: return None

def load_inventory(item_str:str) -> Item:
    print(item_str)
    if not item_str: return []
    item_ids = [int(item_id.strip()) for item_id in item_str.rstrip(',').split(",")]

    items = [db.session.execute(db.select(Item).filter_by(id=item_id)).fetchone() for item_id in item_ids]

    # inventory = [Item(**item[0]) for item in items]
    return [item[0] for item in items]

if __name__ == "__main__":
    create_models()
