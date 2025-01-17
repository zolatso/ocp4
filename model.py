import datetime
import random


class Player:
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = datetime.datetime.strptime(dob, "%d/%m/%Y").date()
        self.total_score = 0
        self.matches_played = 0
        self.tournaments = []

class PlayerManager:
    def __init__(self):
        self.players = []
        self.load()

    def save(self):
        pass

    def load(self):
        pass

class PlayerInTournament:
    def __init__(self, player):
        self.player = player
        self.score_in_tournament = 0

class Tournament:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.place = kwargs['place']
        self.start_date = datetime.datetime.now().date()
        self.number_of_rounds = kwargs.get('number_of_rounds', 4)
        self.current_round = 0
        self.players = self.turn_players_into_tournament_players(kwargs['players'])
        self.description = kwargs['description']
    
    def turn_players_into_tournament_players(self, players):
        new_list = []
        for obj in players:
            new_list.append(PlayerInTournament(obj))
            obj.tournaments.append(self)
        return new_list
    
    def create_first_matches(self, round, players):
        matches = []
        players_copy = players.copy()
        while players_copy:
            playerA = random.choice(players_copy)
            players_copy.remove(playerA)
            playerB = random.choice(players_copy)
            players_copy.remove(playerB)
            match = Match(self, round, playerA, 0, playerB, 0)
            matches.append(match)
        return matches
    
    def create_matches(self, round, players):
        pass
        
    def generate_new_round(self):
        self.current_round += 1
        name_of_round = "Round " + str(self.current_round)
        round = Round(name_of_round)
        if self.current_round == 1:
            matches = self.create_first_matches(round, self.players)
        else:
        # this functionality doesn't work yet as I haven't written the full pair generation function
        # simply repeats fully random generation of pairs
            matches = self.create_first_matches(round, self.players)
        round.matches = matches
        return round


class TournamentManager:
    def __init__(self):
        self.tournaments = []
        self.load()

    def save():
        pass

    def load():
        pass

class Round:
    def __init__(self, name):
        self.name = name
        self.start_date = datetime.datetime.now().date()
        self.matches = []

    def play_matches(self):
        for match in self.matches:
            match.play_match()


class Match:
    """
    Should not be a class, it may just be stocked as a tuple containing two lists, which any has two elements:
    a player and a score
    Ex: ([player_1, 0], [player_2, 1]) is a match
    """
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
        self.playerA.player.matches_played += 1
        self.playerB.player.matches_played += 1

def main():
    pass

if __name__ == '__main__':
    main()

   