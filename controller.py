import os
import json
import random
from model import PlayerManager, TournamentManager
from enum import IntEnum
from views import MainMenuView

# def extract_players():
#     # This function takes the players json file and ranomly selects the passed number into a list of player objects
#     file_to_open = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/players/players.json')
#     with open(file_to_open, 'r') as f:
#         initial_list = json.load(f)
#     converted_list = []
#     for item in initial_list:
#         converted_list.append(Player(item[0], item[1], item[2]))
#     return converted_list

class MainMenuOptions(IntEnum):
    EXIT = 0
    CREATE_TOURNAMENT = 1
    LOAD_TOURNAMENT = 2
    CREATE_PLAYER = 3
    REPORTS = 4

class MainMenu:
    def __init__(self):
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()
        self.menu = MainMenuView()

    def run(self):
        result = -1
        while result != MainMenuOptions.EXIT:
            result = self.menu.input_result()
            result = int(result)