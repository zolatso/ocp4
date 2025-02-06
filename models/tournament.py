import datetime
from random import sample
from models.round import Round

class Tournament:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.place = kwargs.get('place', 'Marseille')
        self.start_date = datetime.datetime.strptime(kwargs['start_date'], "%d/%m/%Y").date()
        self.number_of_rounds = kwargs.get('number_of_rounds', 4)
        #self.current_round = kwargs.get('current_round', 0)
        self.players = kwargs['players']
        self.rounds = kwargs.get('rounds', [])
        self.description = kwargs.get('description', 'No description')
        self.complete = kwargs.get('complete', False)
    
    def create_first_matches(self):
        matches = []
        players_copy = self.players.copy()
        while players_copy:
            pair_of_players = sample(players_copy, 2)
            match = ([pair_of_players[0], 0], [pair_of_players[1], 0])
            players_copy.remove(pair_of_players[0])
            players_copy.remove(pair_of_players[1])
            matches.append(match)
        return matches

    def get_opponents(self, player, paired_players):
        """
        Function takes a player and finds among the other players in the tournament
        Those against whom the player has not played, returning a list of these

        Alternatively, the function returns a list of all the other players in the tournament
        """
        met_opponents = []
        for opponent in self.players:
            # First thing is to check that the player we passed to the function
            # is not the player we are checking while iterating through
            # the list of all players
            if opponent is player:
                continue
            # Once this is verified, we then need to run through all rounds and
            # all matches unless we find that they have played together
            # at which point both round and match loops are broken
            for round in self.rounds:
                for match in round.matches:
                    players_in_match = [match[0][0], match[1][0]]
                    if player in players_in_match and opponent in players_in_match:
                        met_opponents.append(opponent)
                        break
                else:
                    continue
                break

        if (len(met_opponents) == len(self.players) - 1):
            return list(x for x in met_opponents if x not in paired_players)
        else:
            unmet_opponents = list(x for x in self.players if x not in met_opponents)
            unmet_opponents.remove(player)
            unmet_and_unpaired_opponents = list(x for x in unmet_opponents if x not in paired_players) 
            if not unmet_and_unpaired_opponents:
                return list(x for x in met_opponents if x not in paired_players)
            else:
                return unmet_and_unpaired_opponents

    def create_matches(self):
        matches = []
        players = self.players
        ranked_players = list(self.get_ranking().keys())
        paired_players = []
        while len(paired_players) < len(players):
            for player in ranked_players:
                # We first check if the player has already been paired
                if player in paired_players:
                    continue
                # print(f"Trying to pair: {player.first_name} {player.last_name}")
                # Create a list of all players the player has not played against yet
                # If they have played against them all, then return all other players
                # We also pass the list of already paired players
                opponents = self.get_opponents(player, paired_players)
                # the opponent is the highest ranked in the previous list
                opponent = self.find_highest_ranked(opponents, ranked_players)
                match = ([player, 0], [opponent, 0])
                matches.append(match)
                paired_players.append(player)
                paired_players.append(opponent)
        return matches

    def find_highest_ranked(self, objects, ranked_list):
        valid_indices = [
            ranked_list.index(obj) 
            for obj in objects 
            if obj in ranked_list
        ]
        highest_rank_index = min(valid_indices)
        return ranked_list[highest_rank_index]

            
    def generate_new_round(self):
        name_of_round = "Round " + str(len(self.rounds) + 1)
        if len(self.rounds) == 0:
            matches = self.create_first_matches()
        else:
            matches = self.create_matches()
        round = Round(
            name = name_of_round,
            matches = matches
        )
        self.rounds.append(round)
        return round
    
    def get_ranking(self):
        total_scores = []
        for player in self.players:
            pair = []
            pair.append(player)
            score = 0
            for round in self.rounds:
                for match in round.matches:
                    if match[0][0] is player:
                        score += match[0][1]
                        break
                    elif match[1][0] is player:
                        score += match[1][1]
                        break
            pair.append(score)
            total_scores.append(pair)
        ranking = dict(sorted(total_scores, key=lambda item: item[1], reverse=True))
        return ranking
    
def main():
    pass

if __name__ == '__main__':
    main()
