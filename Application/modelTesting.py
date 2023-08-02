"""In this file, we will test creating models!"""
from models.models import *
from os import listdir

base = "./testing/Model/"

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
            if target == -1: target = None

            datum[fields[i]] = target 
        data.append(datum)
    return data


def create_models():
    characters = get_info("characters")
    fighters = get_info("fighters")
    enemies = get_info('enemies')
    base_items = get_info("base")
    # items = get_info("items")
    weapons = get_info("weapons")
    armours = get_info("armours")
    abilities = get_info("abilities")
    passives  = get_info("passives")

    print(characters, fighters, base_items, abilities)


if __name__ == "__main__":
    create_models()
