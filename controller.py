import os
import json
import random
from model import Player

def extract_players():
    # This function takes the players json file and ranomly selects the passed number into a list of player objects
    file_to_open = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/players/players.json')
    with open(file_to_open, 'r') as f:
        initial_list = json.load(f)
    converted_list = []
    for item in initial_list:
        converted_list.append(Player(item[0], item[1], item[2]))
    return converted_list