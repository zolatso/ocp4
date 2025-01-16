import os
import json
import random
from model import Player, PlayerInTournament, Match, Tournament, Round
from views import print_tournament, print_round, print_players
from controller import extract_players

def main():

    players = extract_players()
    
    tournament80 = Tournament('tournament 86533', 'Marseille', 5, random.sample(players, 12), 
                            'le premier tournois du nouvel an')
    
    print_tournament(tournament80)
    
    roundxyz = tournament80.generate_new_round()

    roundxyz.play_matches()

    print_round(roundxyz)

    print_tournament(tournament80)

    roundxyz_2 = tournament80.generate_new_round()

    roundxyz_2.play_matches()

    print_round(roundxyz_2)

    print_tournament(tournament80)

    print_players(players)

    tournament90 = Tournament('tournament 2475957', 'Paris', 5, random.sample(players, 10), 
                            'le deuxieme tournois du nouvel an')
    
    print_tournament(tournament90)
    
    roundabc = tournament90.generate_new_round()

    roundabc.play_matches()

    print_round(roundabc)

    print_tournament(tournament90)

    roundabc_2 = tournament90.generate_new_round()

    roundabc_2.play_matches()

    print_round(roundabc_2)

    print_tournament(tournament90)

    print_players(players)

if __name__ == '__main__':
    main()