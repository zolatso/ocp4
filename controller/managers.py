import os
import json
import datetime
from models.tournament import Tournament
from models.player import Player
from models.round import Round


class PlayerManager:
    """
    Cette classe contrôle le chargement et l'enregistrement des joueurs.
    Elle gère la conversion des données JSON en objets Python et vice versa.
    Une fois chargés, les joueurs sont stockés dans une liste et utilisés par diverses autres classes et fonctions.

    This class controls the loading and saving of players.
    It handles the conversion from JSON data to Python objects and vice versa.
    Once loaded, the players are stored in a list and used by various other classes and functions.
    """

    players_json_file = os.path.join(os.getcwd(), "data/players/players.json")

    def __init__(self):
        self.players = []
        self.load()

    def save(self):
        data = []
        for obj in self.players:
            player = [
                obj.first_name,
                obj.last_name,
                obj.dob.strftime("%d/%m/%Y"),
                obj.identifiant,
            ]
            data.append(player)
        with open(self.players_json_file, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        with open(self.players_json_file, "r") as f:
            initial_list = json.load(f)
        for item in initial_list:
            player = Player(
                first_name=item[0], last_name=item[1], dob=item[2], identifiant=item[3]
            )
            self.players.append(player)


class TournamentManager:
    """
    Cette classe contrôle le chargement et l'enregistrement des tournois (y compris les tours et les matchs).
    Elle gère la conversion des données JSON en objets Python et vice versa.
    Une fois chargés, les joueurs sont stockés dans une liste et utilisés par diverses autres classes et fonctions.

    This class controls the loading and saving of tournaments (including rounds and matches).
    It handles the conversion from JSON data to Python objects and vice versa.
    Once loaded, the tournaments are stored in a list and used by various other classes and functions.
    """

    def __init__(self, players):
        self.tournaments = []
        self.players = players
        self.load()

    def convert_to_dict(self, tournament):
        """
        Cette fonction prend un objet tournoi (y compris ses tours et matchs)
        et prépare un dictionnaire adapté à l'enregistrement sous forme de données JSON.
        Elle est appelée par la fonction save au sein de cette classe.

        This function takes a tournament object (including its rounds and matches)
        and prepares a dictionary that is suitable for saving as JSON data.
        It is called by the function save within this class.
        """
        data = {}
        data["name"] = tournament.name
        data["place"] = tournament.place
        data["date"] = tournament.start_date.strftime("%d/%m/%Y")
        data["number_of_rounds"] = tournament.number_of_rounds
        data["players"] = []
        for player in tournament.players:
            full_name = player.first_name + " " + player.last_name
            data["players"].append(full_name)
        data["rounds"] = []
        for round in tournament.rounds:
            individual_round = {}
            individual_round["name"] = round.name
            individual_round["start_date"] = round.start_date.strftime("%d/%m/%Y")
            matches = []
            for match in round.matches:
                player_and_score_a = [
                    match[0][0].first_name + " " + match[0][0].last_name,
                    match[0][1],
                ]
                player_and_score_b = [
                    match[1][0].first_name + " " + match[1][0].last_name,
                    match[1][1],
                ]
                pair = [player_and_score_a, player_and_score_b]
                matches.append(pair)
            individual_round["matches"] = matches
            individual_round["complete"] = round.complete
            data["rounds"].append(individual_round)
        data["description"] = tournament.description
        data["complete"] = tournament.complete
        return data

    def save_to_file(self, data):
        """
        Cette fonction gère le processus d'écriture des données JSON dans le fichier.
        Elle est appelée par la fonction save au sein de cette classe.

        This function handles the process of writing the JSON data to the file.
        It is called by the function save within this class.
        """
        json_save_folder = "data/tournaments"
        file_name = data["name"] + ".json"
        json_file_path = os.path.join(json_save_folder, file_name)
        with open(json_file_path, "w") as f:
            json.dump(data, f, indent=4)

    def save(self):
        """
        Cette fonction appelle les fonctions nécessaires pour convertir les objets
        en dictionnaires et les enregistrer sous forme de fichiers JSON.

        This function calls the functions that are required in order to
        convert objects to dictionaries and save them as JSON files.
        """
        for item in self.tournaments:
            data = self.convert_to_dict(item)
            self.save_to_file(data)

    def load(self):
        files = self.load_from_dir()
        for file in files:
            with open(file, "r") as f:
                data = json.load(f)
            players = self.match_player_objects_to_json(data["players"], self.players)
            rounds = self.create_rounds_from_json(data["rounds"], players)
            tournament = Tournament(
                name=data["name"],
                place=data["place"],
                # start_date = datetime.datetime.strptime(data['date'], "%d/%m/%Y").date(),
                start_date=data["date"],
                number_of_rounds=data["number_of_rounds"],
                players=players,
                rounds=rounds,
                description=data["description"],
                complete=data["complete"],
            )
            self.tournaments.append(tournament)

    def load_from_dir(self):
        folder = os.path.join(os.getcwd(), "data/tournaments/")
        files = os.listdir(folder)
        files = [os.path.join(folder, item) for item in files]
        return files

    def match_player_objects_to_json(self, json, objects):
        processed_list = [item.split() for item in json]
        players = []
        for item in processed_list:
            for obj in objects:
                if item[0] == obj.first_name and item[1] == obj.last_name:
                    players.append(obj)
                    break
        return players

    def create_rounds_from_json(self, json, players):
        rounds = []
        for dict in json:
            name = dict["name"]
            start_date = datetime.datetime.strptime(
                dict["start_date"], "%d/%m/%Y"
            ).date()
            complete = dict["complete"]
            matches = []
            for item in dict["matches"]:
                player_a = self.match_player_objects_to_json([item[0][0]], players)[0]
                player_b = self.match_player_objects_to_json([item[1][0]], players)[0]
                player_a_score = item[0][1]
                player_b_score = item[1][1]
                match = ([player_a, player_a_score], [player_b, player_b_score])
                matches.append(match)
            round = Round(
                name=name, start_date=start_date, matches=matches, complete=complete
            )
            rounds.append(round)
        return rounds
