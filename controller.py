import os
import json
import random
from model import PlayerManager, TournamentManager
from enum import IntEnum
from views import MainMenuView, ReportMenuView, CreatePlayerView

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
            3: lambda self: self.create_player(),
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

    def create_player(self):
        pass

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
        options = {
            1: lambda self: self.all_players(),
            2: lambda self: self.tournament_display('details'),
            3: lambda self: self.tournament_display('players'),
            4: lambda self: self.tournament_display('rounds')
            #5: lambda self: self.tournament_display('ranking')
        }
        result = None
        while result != ReportsMenuOptions.EXIT:
            self.menu.prompt_options()
            result = self.menu.input_result()
            result = int(result)
            if result != 0:
                try:
                    options[result](self)
                except KeyError:
                    self.menu.invalid_option(result)

    def all_players(self):
        self.menu.all_players(self.player_manager.players)

    def tournament_display(self, aspect):
        tournaments = self.tournament_manager.tournaments
        result = self.menu.choose_tournament(tournaments, aspect)
        for index, obj in enumerate(tournaments):
            if int(result) == index:
                self.menu.tournament_display(obj, aspect)
            
    # def tournament_players(self):
    #     tournaments = self.tournament_manager.tournaments
    #     result = self.menu.choose_tournament(tournaments, 'players')
    #     for index, obj in enumerate(tournaments):
    #         if int(result) == index:
    #             self.menu.tournament_players(obj)

    # def tournament_rounds(self):
    #     tournaments = self.tournament_manager.tournaments
    #     result = self.menu.choose_tournament(tournaments, 'rounds')
    #     for index, obj in enumerate(tournaments):
    #         if int(result) == index:
    #             self.menu.tournament_rounds(obj)