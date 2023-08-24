"""This file is responsible for loading the data from the files, and adding them to the game's database."""

from requests import post 
from json import dumps
from os.path import exists
from sys import argv

base = "./data/"
URL = "http://127.0.0.1:20000/add/"

def readlines(filename:str) -> list:
    """As it sounds, this method is responsible for reading the lines of a given file, and returning a list of each line stripped of trailing whitespace.
    
    Args:
        filename (str): The name of the file to parse.
        
    Returns:
        list"""
    if not exists(base+filename+".txt"):
        print(base+filename, "could not be found.")
        return []
    
    with open(base+filename+".txt") as fp:
        lines = fp.readlines()

    if len(lines) < 1: 
        print("No lines could be found in", filename)
        return []
    return [line.strip() for line in lines]

def get_info(filename, sep=" | ") -> list:
    """This method parses the information from a given file and returns the result as a list of dictionaries.
    
    Args:
        filename (str): The name of the file to read.
        sep (str): The value to separte the fields of the file by. Defaults to ' | '
        
    Returns:
        List of dictionaries, each dictionary containing the parsed line of the file."""
    
    lines = readlines(filename)
    if not lines: return []
    fields = lines[0].split(sep)
    data = []

    for line in lines[1:]:
        l = line.split(sep)
        datum = {}
        for i in range(len(fields)):
            target: str = l[i]
            if "_" in target: target = target.replace("_", " ")
            if target.isnumeric(): target = int(target)
            if target in [-1, "-1"]: target = None

            datum[fields[i]] = target 
        data.append(datum)
    
    return data

def make_request(endpoint:str, items:list) -> None:
    """This method is responsible for making the requests to the game servers to add the items from the file to the database.
    
    Args:
        endpoint (str): The URL to 'hit' for the chosen data.
        items (list): The list of dictionaries created from the get_info function.
        
    Returns:
        None"""
    
    for item in items:
        try:
            resp = post(URL+endpoint+"/", json=dumps(item))
            resp.raise_for_status()
            print(resp.json())
        except:
            print("An error occurred for ", item)

def get_info_and_request(filename:str, endpoint:str, sep=' | '):
    """Gets info from a file, and sends the request to the endpoint.
    
    Args:
        filename (str): The name of the file to parse.
        endpoint (str): The API endpoint to target.
        sep (str): The delimiter for the file."""
    
    info = get_info(filename, sep)
    make_request(endpoint, info)

# dictionary mapping filenames to their API routes
filenames = {
    "abilities": {'endpoint': "item"},
    "armours": {'endpoint': "item"},
    "items": {'endpoint': "item"},
    "passives": {'endpoint': "item"},
    "weapons": {'endpoint': "item"},
    "enemies": {'endpoint': "enemy"},
    "jobs": {'endpoint': "job"},
    "stats": {'endpoint': "stats"},
}

def add_models():
    if (len(argv) == 1):
        print("Did you know that you can run this program with Command line arguments to only add certain files? Just include the name of the file to add!")

    files = argv[1:] if len(argv) > 1 else list(filenames.keys())

    for file in files:
        if file not in filenames:
            print(file, "is not a valid filename for an API route.")
            continue

        info = get_info(file, filenames[file].get('sep', " | "))
        if not info: continue

        make_request(filenames[file]['endpoint'], info)

if __name__ == "__main__":
    add_models()