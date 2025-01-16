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

class PlayerInTournament:
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
            obj.tournaments.append(self)
        return new_list
    
    def create_first_list_of_matches(self, round, players):
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
    
    def create_list_of_matches(self, round, players):
        pass
        
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
        self.playerA.player.matches_played += 1
        self.playerB.player.matches_played += 1

def main():
    pass

if __name__ == '__main__':
    main()

   