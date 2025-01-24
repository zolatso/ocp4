import os
import json
import random
from model import PlayerManager, TournamentManager
from enum import IntEnum
from views import MainMenuView, ReportMenuView

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
        self.tournament_manager = TournamentManager(self.player_manager.players)
        self.menu = MainMenuView()
        self.reports_menu = None

    def run(self):
        options = {
            1: lambda self: self.create_tournament(),
            2: lambda self: self.load_tournament(),
            3: lambda self: self.create_tournament(),
            4: lambda self: self.load_report_menu()
        }

        result = None
        while result != MainMenuOptions.EXIT:
            self.menu.prompt_options()
            result = self.menu.input_result()
            result = int(result)
            # Except 0 as it's the exit option
            if result != 0:
                try:
                    options[result](self)
                except KeyError:
                    self.menu.invalid_option(result)

    def load_report_menu(self):
        if not self.reports_menu:
            self.reports_menu = ReportsMenu(self.tournament_manager, self.player_manager)
        self.reports_menu.run()

class ReportsMenuOptions(IntEnum):
    EXIT = 0
    ALL_PLAYERS = 1
    ALL_TOURNAMENTS = 2
    TOURNAMENT_DETAIL = 3
    TOURNAMENT_PLAYERS = 4
    TOURNAMENT_ROUNDS = 5

class ReportsMenu:
    def __init__(self, tournament_manager, player_manager):
        self.tournament_manager = tournament_manager
        self.player_manager = player_manager
        self.menu = ReportMenuView()

    def run(self):
        result = None
        while result != ReportsMenuOptions.EXIT:
            self.menu.prompt_options()
            result = self.menu.input_result()
            result = int(result)