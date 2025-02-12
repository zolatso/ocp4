import re
from controller.managers import PlayerManager, TournamentManager
from enum import IntEnum
from views.menu_views import MainMenuView, ReportMenuView, TournamentMenuView
from controller.create import CreatePlayer, CreateTournament


class MainMenuOptions(IntEnum):
    EXIT = 0
    CREATE_TOURNAMENT = 1
    MODIFY_TOURNAMENT = 2
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
            MainMenuOptions.CREATE_TOURNAMENT: lambda self: self.create_tournament(),
            MainMenuOptions.MODIFY_TOURNAMENT: lambda self: self.modify_tournaments_menu(),
            MainMenuOptions.CREATE_PLAYER: lambda self: self.create_player(),
            MainMenuOptions.REPORTS: lambda self: self.load_report_menu(),
        }

        result = None
        while result != MainMenuOptions.EXIT:
            self.menu.prompt_options()
            result = self.menu.input_result()
            if represents_int(result):
                result = int(result)
                # Except 0 as it's the exit option
                if result != 0:
                    try:
                        options[result](self)
                    except KeyError:
                        self.menu.invalid_option(result)
            else:
                self.menu.invalid_input()

    def load_report_menu(self):
        if not self.reports_menu:
            self.reports_menu = ReportsMenu(
                self.tournament_manager, self.player_manager
            )
        self.reports_menu.run()

    def modify_tournaments_menu(self):
        if not self.tournaments_menu:
            self.tournaments_menu = TournamentsMenu(
                self.tournament_manager, self.player_manager
            )
        self.tournaments_menu.run()

    def create_player(self):
        create_player = CreatePlayer(self.player_manager)
        create_player.run()

    def create_tournament(self):
        create_tournament = CreateTournament(
            self.tournament_manager, self.player_manager
        )
        create_tournament.run()


class ReportsMenuOptions(IntEnum):
    EXIT = 0
    ALL_PLAYERS = 1
    ALL_TOURNAMENTS = 2
    TOURNAMENT_DETAIL = 3
    TOURNAMENT_PLAYERS = 4


class ReportsMenu:
    def __init__(self, tournament_manager, player_manager):
        self.tournament_manager = tournament_manager
        self.player_manager = player_manager
        self.menu = ReportMenuView()

    def run(self):
        options = {
            ReportsMenuOptions.ALL_PLAYERS: lambda self: self.all_players(),
            ReportsMenuOptions.ALL_TOURNAMENTS: lambda self: self.tournament_display(
                "details"
            ),
            ReportsMenuOptions.TOURNAMENT_DETAIL: lambda self: self.tournament_display(
                "players"
            ),
            ReportsMenuOptions.TOURNAMENT_PLAYERS: lambda self: self.tournament_display(
                "rounds"
            ),
            # 5: lambda self: self.tournament_display('ranking')
        }
        result = None
        while result != ReportsMenuOptions.EXIT:
            self.menu.prompt_options()
            result = self.menu.input_result()
            if represents_int(result):
                result = int(result)
                if result != 0:
                    try:
                        options[result](self)
                    except KeyError:
                        self.menu.invalid_option(result)
            else:
                self.menu.invalid_input()

    def all_players(self):
        players = sorted(
            self.player_manager.players, key=lambda player: player.last_name
        )
        self.menu.all_players(players)

    def tournament_display(self, aspect):
        tournaments = self.tournament_manager.tournaments
        result = self.menu.choose_tournament(tournaments, aspect)
        for index, tournament in enumerate(tournaments):
            if int(result) == index:
                self.menu.tournament_display(tournament, aspect)


class TournamentsMenuOptions(IntEnum):
    EXIT = 0
    ADD_ROUND = 1
    INPUT_SCORES = 2


class TournamentsMenu:
    def __init__(self, tournament_manager, player_manager):
        self.tournament_manager = tournament_manager
        self.player_manager = player_manager
        self.menu = TournamentMenuView()

    def choose_tournament(self, tournaments):
        while True:
            unfinished_tournaments = []
            for obj in tournaments:
                if not obj.complete:
                    unfinished_tournaments.append(obj)
            result = self.menu.choose_tournament(unfinished_tournaments)
            for index, obj in enumerate(unfinished_tournaments):
                if index == int(result):
                    return obj

    def run(self):

        tournament = self.choose_tournament(self.tournament_manager.tournaments)

        options = {
            TournamentsMenuOptions.ADD_ROUND: lambda self, tournament: self.generate_new_round(
                tournament
            ),
            TournamentsMenuOptions.INPUT_SCORES: lambda self, tournament: self.input_scores(
                tournament
            ),
        }
        result = None
        while result != TournamentsMenuOptions.EXIT:
            self.menu.prompt_options(tournament)
            result = int(self.menu.input_result())
            if represents_int(result):
                result = int(result)
                if result != 0:
                    try:
                        options[result](self, tournament)
                    except KeyError:
                        self.menu.invalid_option(result)
            else:
                self.menu.invalid_input()

    def generate_new_round(self, tournament):
        if tournament.rounds:
            if not tournament.rounds[-1].complete:
                self.menu.error_msg(
                    "The current round is not complete. Please input scores before gnerating a new round."
                )
                return False
            if tournament.complete:
                self.menu.error_msg(
                    "This tournament is now complete. Please exit the menu and choose another option"
                )
                return False
        round = tournament.generate_new_round()
        self.menu.successful_pair_generation(tournament, round)
        self.tournament_manager.save()

    def get_scores(self, match, index):
        while True:
            result = self.menu.input_scores(match, index)
            pattern = r"^[1-3]$"
            if re.match(pattern, result):
                result = int(result)
                if result == 1:
                    scores = [1, 0]
                elif result == 2:
                    scores = [0, 1]
                elif result == 3:
                    scores = [0.5, 0.5]
                return scores
            else:
                self.menu.error_msg("Please enter either 1, 2, or 3")

    def input_scores(self, tournament):
        if len(tournament.rounds) == 0:
            self.menu.error_msg(
                "No rounds have been created for this tournament. Please generate round first"
            )
            return False

        round = tournament.rounds[-1]

        if round.complete:
            self.menu.error_msg(
                "The current round is already complete. Please generate a new round first."
            )
            return False

        for i in range(len(round.matches)):
            scores = self.get_scores(round.matches[i], i)
            round.matches[i][0][1] = scores[0]
            round.matches[i][1][1] = scores[1]
        self.menu.successful_score_entry(tournament)
        round.complete = True
        if len(tournament.rounds) == tournament.number_of_rounds:
            tournament.complete = True
        self.tournament_manager.save()


def represents_int(s):
    """
    Une fonction d'aide qui vérifie si les entrées du menu peuvent être converties
    en nombres entiers

    A helper function that checks if menu inputs can be converted
    into integers
    """
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True
        
