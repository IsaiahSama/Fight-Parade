"""In this file, we will test creating models!"""
from requests import post
from json import dumps

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
    # items = get_info("items")
    characters = get_info("characters")
    fighters = get_info("fighters")
    enemies = get_info('enemies')
    base_items = get_info("base")
    weapons = get_info("weapons")
    armours = get_info("armours")
    abilities = get_info("abilities")
    passives  = get_info("passives")

    # Making the requests to update for fighter
    c = [character for character in characters if character['id'] == fighters[0]['id']]
    print(c)
    c[0].update(fighters[0])
    print(dumps(c[0]))
    # print(data)
    res = post(URL+"user/", json=dumps(c[0]))
    res.raise_for_status()
    print(res.json())

if __name__ == "__main__":
    create_models()
