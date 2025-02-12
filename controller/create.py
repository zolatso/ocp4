import re
from views.create_views import CreatePlayerView, CreateTournamentView
from models.player import Player
from models.tournament import Tournament


class CreatePlayer:
    """
    Cette option gère les vues et valide les entrées pour
    lorsqu'un utilisateur souhaite créer un nouveau jouer. Après avoir créé l'objet
    joueur valide, elle l'ajoute à la classe PlayerManager et l'enregistre.

    This option manages the views and validates the inputs for
    when a user wants to create a new player. After creating the
    valid player object, it adds it to PlayerManager class and saves it.
    """

    def __init__(self, player_manager):
        self.player_manager = player_manager
        self.view = CreatePlayerView()

    def get_input(self, aspect, pattern):
        """
        Obtient les données pertinentes et les vérifie par rapport au modèle de regex transmis à la fonction.
        Obtains relevant input and checks it against regex pattern that is passed to function.
        """
        while True:
            result = self.view.input(aspect)
            if re.match(pattern, result):
                return result
            else:
                self.view.error_msg()

    def run(self):
        """
        Il contrôle le fonctionnement général de la classe et de ses fonctions.
        This controls the overall operation of the class and its functions.
        """
        results = []
        inputs = {
            "first name": r"^[a-zA-Z]+$",
            "last name": r"^[a-zA-Z]+$",
            "date of birth": r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(19|20)\d{2}$",
            "identifiant": r"^[A-Z]{2}[0-9]{5}$",
        }
        for key, value in inputs.items():
            results.append(self.get_input(key, value))

        new_player = Player(
            first_name=results[0],
            last_name=results[1],
            dob=results[2],
            identifiant=results[3],
        )
        self.player_manager.players.append(new_player)
        self.player_manager.save()
        self.view.success_msg(new_player)


class CreateTournament:
    """
    Cette option gère les vues et valide les entrées pour
    lorsqu'un utilisateur souhaite créer un nouveau tournois. Après avoir créé l'objet
    tournois valide, elle l'ajoute à la classe TournamentManager et l'enregistre.

    This option manages the views and validates the inputs for
    when a user wants to create a new tournament. After creating the
    valid tournament object, it adds it to TournamentManager class and saves it.
    """

    def __init__(self, tournament_manager, player_manager):
        self.tournament_manager = tournament_manager
        self.player_manager = player_manager
        self.view = CreateTournamentView()

    def get_input(self, aspect, pattern, error):
        while True:
            result = self.view.input(aspect)
            if re.match(pattern, result):
                return result
            else:
                self.view.error_msg(error)

    def get_player_list(self):
        """
        Cette fonction présente la liste des joueurs et vérifie que l'utilisateur a sélectionné un nombre approprié.
        sélectionné un numéro approprié.

        This function presents the list of players and checks that the user has
        selected an appropriate number.
        """
        while True:
            result = self.view.choose_players(self.player_manager.players)
            if re.match(r"^\s*(\d+\s*)*\d+\s*$", result):
                list = [int(item) for item in result.split()]
                valid = True
                if not len(list) % 2 == 0:
                    self.view.error_msg("List contains an odd number of players")
                    valid = False
                for item in list:
                    if item > len(self.player_manager.players):
                        self.view.error_msg(
                            "List contains numbers that are not in the player list"
                        )
                        valid = False
                        break
                if valid:
                    return list
            else:
                self.view.error_msg(
                    "This is not a list of integers separated by spaces"
                )

    def get_input_patterns(self):
        """
        Cette fonction définit les modèles d'entrée nécessaires aux différents composants du tournoi.
        Elle existe pour que la fonction d'exécution principale ne soit pas trop longue.

        This function defines the input patterns needed for different components of tournament.
        It exists so that the main run function is not too long.
        """
        inputs = {
            "name": [r"^(?!\s*$).+", "Must contain at least one character"],
            "location": [r"^(?!\s*$).+", "Must contain at least one character"],
            "start date": [
                r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(19|20)\d{2}$",
                "date in format: DD/MM/YYYY",
            ],
            "number of rounds": [
                r"^([0-9]|1[0-9]|20)$",
                "Must be an integer of 20 or less",
            ],
            "description": [r"^(?!\s*$).+", "must contain at least one character"],
        }
        return inputs

    def run(self):
        """
        Il contrôle le fonctionnement général de la classe et de ses fonctions.
        This controls the overall operation of the class and its functions.
        """
        results = {}
        inputs = self.get_input_patterns()

        # Creates different input sequences
        for key, value in inputs.items():
            input = self.get_input(key, value[0], value[1])
            if input:
                results[key] = input
            else:
                results[key] = None

        # Controls the player selection
        player_selection = self.get_player_list()
        players = []
        for item in player_selection:
            for index, obj in enumerate(self.player_manager.players):
                if int(item) == index:
                    players.append(obj)

        # Creates the class
        new_tournament = Tournament(
            **{
                k: v
                for k, v in {
                    "name": results["name"],
                    "location": results["location"],
                    "number_of_rounds": int(results["number of rounds"]),
                    "description": results["description"],
                    "start_date": results["start date"],
                    "players": players,
                }.items()
                if v is not None
            }
        )

        self.tournament_manager.tournaments.append(new_tournament)
        self.tournament_manager.save()
        self.view.success_msg()
