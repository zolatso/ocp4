import json
import os
import datetime
import random
from views import print_tournament

class Player:
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = datetime.datetime.strptime(dob, "%d/%m/%Y").date()
        self.total_score = 0

class PlayerInTournament():
    def __init__(self, player):
        self.player = player
        self.score_in_tournament = 0

class Tournament:
    def __init__(self, name, place, number_of_rounds, list_of_players,
                description):
        self.name = name
        self.place = place
        self.start_date = datetime.datetime.now().date()
        self.number_of_rounds = 4 if number_of_rounds == 0 else number_of_rounds
        self.current_round = 0
        self.list_of_players = self.turn_players_into_tournament_players(list_of_players)
        self.description = description
    
    def turn_players_into_tournament_players(self, players):
        new_list = []
        for obj in players:
            new_list.append(PlayerInTournament(obj))
        return new_list
    
    def create_first_list_of_matches(self, round, players):
        matches = []
        players_copy = players.copy()
        while players_copy:
            playerA = random.choice(players_copy)
            players_copy.remove(playerA)
            playerB = random.choice(players_copy)
            players_copy.remove(playerB)
            match = Match(self.name, round, playerA, 0, playerB, 0)
            matches.append(match)
        return matches
        
    def generate_new_round(self):
        self.current_round += 1
        name_of_round = "Round " + str(self.current_round)
        round = Round(name_of_round, self)
        if self.current_round == 1:
            matches = self.create_first_list_of_matches(round, self.list_of_players)
        else:
        # this functionality doesn't work yet as I haven't written the full pair generation function
        # simply repeats fully random generation of pairs
            matches = self.create_first_list_of_matches(round, self.list_of_players)
        round.list_of_matches = matches
        return round


class Round:
    def __init__(self, name, tournament):
        self.name = name
        self.tournament = tournament
        self.start_date = datetime.datetime.now().date()
        self.list_of_matches = []

    #def update_player_scores_in_tournament(self):
    #    player_list = self.tournament.list_of_players
    #    for player_object in self.list_of_matches:
    #        for item in enumerate(player_list):
    #            if item[0] is player_object.playerA:
    #                item[1] = player_object.playerA_score
    #            if item[0] is player_object.playerB:
    #                item[1] = player_object.playerB_score

    def update_player_total_scores(self):
        pass

    def play_matches(self):
        for match in self.list_of_matches:
            match.play_match()


class Match:
    def __init__(self, tournament, round, playerA, playerA_score, playerB, playerB_score):
        self.tournament = tournament
        self.round = round
        self.playerA = playerA
        self.playerA_score = playerA_score
        self.playerB = playerB
        self.playerB_score = playerB_score

    def play_match(self):
        possibilities = [1, 2, 3]
        roll_the_dice = random.choice(possibilities)
        if (roll_the_dice == 1):
            self.playerA_score = 1
            self.playerB_score = 0
        elif (roll_the_dice == 2):
            self.playerA_score = 0
            self.playerB_score = 1
        elif (roll_the_dice == 3):
            self.playerA_score = 0.5
            self.playerB_score = 0.5
        # These lines update both the tournament overall score and
        # the player overall score
        self.playerA.score_in_tournament += self.playerA_score
        self.playerB.score_in_tournament += self.playerB_score
        self.playerA.player.total_score += self.playerA_score
        self.playerB.player.total_score += self.playerB_score

def extract_players(n):
    # This function takes the players json file and ranomly selects the passed number into a list of player objects
    file_to_open = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/players/players.json')
    with open(file_to_open, 'r') as f:
        initial_list = json.load(f)
    converted_list = []
    for i in range(n):
        selection = random.choice(initial_list)
        converted_list.append(PlayerInTournament(selection[0], selection[1], selection[2]))
        initial_list.remove(selection)
    return converted_list

def main():

    
    tournament80 = Tournament('tournament 86533', 'Marseille', 5, extract_players(6), 
                            'le premier tournois du nouvel an')


    roundxyz = tournament80.generate_new_round()
    
    print(roundxyz.list_of_matches)
    #print_tournament(tournament80)


if __name__ == '__main__':
    main()

   