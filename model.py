import datetime
import os
import json
from random import choice, sample


class Player:
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = datetime.datetime.strptime(dob, "%d/%m/%Y").date()
        self.total_score = 0
        self.matches_played = 0
        self.tournaments = []

    def score_in_tournament(self, tournament):
        pass

    def total_score(self):
        pass
        

class PlayerManager:
    def __init__(self):
        self.players = []
        self.load()

    def save(self):
        pass

    def load(self):
        file_to_open = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/players/players.json')
        with open(file_to_open, 'r') as f:
            initial_list = json.load(f)
        for item in initial_list:
            self.players.append(Player(item[0], item[1], item[2]))
    

#class PlayerInTournament:
#    def __init__(self, player):
#        self.player = player
#        self.score_in_tournament = 0


class Tournament:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.place = kwargs['place']
        self.start_date = datetime.datetime.now().date()
        self.number_of_rounds = kwargs.get('number_of_rounds', 4)
        self.current_round = 0
        self.players = kwargs['players']
        self.rounds = []
        self.description = kwargs['description']
    
    # def turn_players_into_tournament_players(self, players):
    #     new_list = []
    #     for obj in players:
    #         new_list.append(PlayerInTournament(obj))
    #         obj.tournaments.append(self)
    #     return new_list
    
    def create_first_matches(self, players):
        matches = []
        players_copy = players.copy()
        while players_copy:
            pair_of_players = sample(players_copy, 2)
            match = ([pair_of_players[0], 0], [pair_of_players[1], 0])
            players_copy.remove(pair_of_players[0])
            players_copy.remove(pair_of_players[1])
            matches.append(match)
        return matches
    
    def create_matches(self, round, players):
        pass
        
    def generate_new_round(self):
        self.current_round += 1
        name_of_round = "Round " + str(self.current_round)
        round = Round(name_of_round)
        if self.current_round == 1:
            matches = self.create_first_matches(self.players)
        else:
        # this functionality doesn't work yet as I haven't written the full pair generation function
        # simply repeats fully random generation of pairs
            matches = self.create_first_matches(self.players)
        round.matches = matches
        self.rounds.append(round)
        return round


class TournamentManager:
    def __init__(self, tournaments):
        self.tournaments = [tournaments]

    def save(self):
        json_save_folder = create_dir('data/tournaments')
        for item in self.tournaments:
            data = {}
            data['name'] = item.name
            data['place'] = item.place
            data['date'] = item.start_date.strftime("%d/%m/%Y")
            data['number_of_rounds'] = item.number_of_rounds
            data['current_round'] = item.current_round
            data['players'] = []
            for player in item.players:
                full_name = player.first_name + ' ' + player.last_name
                data['players'].append(full_name)
            data['rounds'] = []
            for round in item.rounds:
                data['rounds'].append(round.name)
                data['rounds'].append(round.start_date.strftime("%d/%m/%Y"))
                matches = []
                for match in round.matches:
                    player_and_score_a = [match[0][0].first_name + ' ' + match[0][0].last_name, match[0][1]]
                    player_and_score_b = [match[1][0].first_name + ' ' + match[1][0].last_name, match[1][1]]
                    pair = [player_and_score_a, player_and_score_b]
                    matches.append(pair)
                data['rounds'].append(matches)
            data['description'] = item.description
            
            file_name = item.name + '.json'
            json_file_path = os.path.join(json_save_folder, file_name)
            with open(json_file_path, 'w') as f:
                json.dump(data, f, indent = 4)

    def load():
        pass

class Round:
    def __init__(self, name):
        self.name = name
        self.start_date = datetime.datetime.now().date()
        self.matches = []

    def play_matches(self):
        for match in self.matches:
            possibilities = [1, 2, 3]
            roll_the_dice = choice(possibilities)        
            if (roll_the_dice == 1):
                match[0][1] = 1
                match[1][1] = 0
            elif (roll_the_dice == 2):
                match[0][1] = 0
                match[1][1] = 1
            elif (roll_the_dice == 3):
                match[0][1] = 0.5
                match[1][1] = 0.5
            
def create_dir(name):
    current_folder = os.getcwd()
    new_folder = name
    new_path = os.path.join(current_folder, new_folder)
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
    return new_path



#class Match:
    # """
    # Should not be a class, it may just be stocked as a tuple containing two lists, which any has two elements:
    # a player and a score
    # Ex: ([player_1, 0], [player_2, 1]) is a match
    # """
    # def __init__(self, tournament, round, playerA, playerA_score, playerB, playerB_score):
    #     self.tournament = tournament
    #     self.round = round
    #     self.playerA = playerA
    #     self.playerA_score = playerA_score
    #     self.playerB = playerB
    #     self.playerB_score = playerB_score

    # def play_match(self):
    #     
    #     # These lines update both the tournament overall score and
    #     # the player overall score
    #     self.playerA.score_in_tournament += self.playerA_score
    #     self.playerB.score_in_tournament += self.playerB_score
    #     self.playerA.player.total_score += self.playerA_score
    #     self.playerB.player.total_score += self.playerB_score
    #     self.playerA.player.matches_played += 1
    #     self.playerB.player.matches_played += 1

def main():

    load_players = PlayerManager()

if __name__ == '__main__':
    main()

   