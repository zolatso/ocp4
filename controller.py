import os
import json
import random
import re
from model import PlayerManager, TournamentManager, Player, Tournament
from enum import IntEnum
from views import MainMenuView, ReportMenuView, CreatePlayerView, CreateTournamentView, TournamentMenuView

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
        self.tournaments_menu = None

    def run(self):
        options = {
            1: lambda self: self.create_tournament(),
            2: lambda self: self.modify_tournaments_menu(),
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

    def modify_tournaments_menu(self):
        if not self.tournaments_menu:
            self.tournaments_menu = TournamentsMenu(self.tournament_manager, self.player_manager)
        self.tournaments_menu.run()

    def create_player(self):
        create_player = CreatePlayer(self.player_manager)
        create_player.run()

    def create_tournament(self):
        create_tournament = CreateTournament(self.tournament_manager, self.player_manager)
        create_tournament.run()
    

class CreatePlayer:
    def __init__(self, player_manager):
        self.player_manager = player_manager
        self.view = CreatePlayerView()

    def get_input(self, aspect, pattern):
        while True:
            result = self.view.input(aspect)
            if re.match(pattern, result):
                return result
            else:
                self.view.error_msg()

    def run(self):
        results = []
        inputs = {
            'first name' : r'^[a-zA-Z]+$',
            'last name' : r'^[a-zA-Z]+$',
            'date of birth' : r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(19|20)\d{2}$',
            'identifiant' : r'^[A-Z]{2}[0-9]{4}$'
        }
        for key, value in inputs.items():
            results.append(self.get_input(key, value))

        new_player = Player(
            first_name = results[0], 
            last_name = results[1],
            dob = results[2],
            identifiant = results[3]
        )
        self.player_manager.players.append(new_player)
        self.player_manager.save()


class CreateTournament:
    def __init__(self, tournament_manager, player_manager):
        self.tournament_manager = tournament_manager
        self.player_manager = player_manager
        self.view = CreateTournamentView()

    def get_input(self, aspect, pattern):
        while True:
            result = self.view.input(aspect)
            regex = re.compile(pattern, re.DOTALL)
            if regex.match(result):
                return result
            else:
                self.view.error_msg()

    def run(self):
        results = []
        inputs = {
            'name' : r".*",
            'location' : r".*",
            'number of rounds' : r".*",
            'description' : r".*",
        }
        for key, value in inputs.items():
            results.append(self.get_input(key, value))
        
        player_selection = self.view.choose_players(self.player_manager.players).split()
        players = []
        for item in player_selection:
            for index, obj in enumerate(self.player_manager.players):
                if int(item) == index:
                    players.append(obj)
        
        new_tournament = Tournament(
            name = results[0],
            location = results[1],
            number_of_rounds = results[2],
            description = results[3],
            players = players
        )

        self.tournament_manager.tournaments.append(new_tournament)
        self.tournament_manager.save()


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

class TournamentsMenuOptions(IntEnum):
    EXIT = 0
    ADD_ROUND = 1
    INPUT_SCORES = 2


class TournamentsMenu:
    def __init__(self, tournament_manager, player_manager):
        self.tournament_manager = tournament_manager
        self.player_manager = player_manager
        self.menu = TournamentMenuView()

    def run(self):
        result = self.menu.choose_tournament(self.tournament_manager.tournaments)
        for index, obj in enumerate(self.tournament_manager.tournaments): 
            if index == int(result):
                tournament = obj

        options = {
            1: lambda self, tournament: self.generate_new_round(tournament),
            2: lambda self, tournament: self.input_scores(tournament)
        }
        result = None
        while result != TournamentsMenuOptions.EXIT:
            self.menu.prompt_options(tournament)
            result = int(self.menu.input_result())
            if result != 0:
                try:
                    options[result](self, tournament)
                except KeyError:
                    self.menu.invalid_option(result)

    def generate_new_round(self, tournament):
        tournament.generate_new_round()
        self.menu.successful_pair_generation(tournament)
        self.tournament_manager.save()

    def input_scores(self, tournament):
        round = tournament.rounds[-1]
        for i in range(len(round.matches)):
            scores = self.menu.input_scores(round.matches[i], i).split()
            round.matches[i][0][1] = scores[0]
            round.matches[i][1][1] = scores[1]
        self.menu.successful_score_entry(tournament)
        self.tournament_manager.save()

    

        
        
    

        
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