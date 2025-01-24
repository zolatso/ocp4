import os
import json
from random import sample, random, randrange
from model import Tournament, Round, PlayerManager, TournamentManager, Player
from views import print_tournament, print_round, print_players
from controller import MainMenu
# from controller import extract_players

def main():
    # main_menu = MainMenu()
    # main_menu.run()

    load_players = PlayerManager()
    load_tournaments = TournamentManager(load_players.players)
    load_tournaments.load()
    tournaments = load_tournaments.tournaments

    tournament_name = "Tournament" + str(randrange(0, 10000000000)) 
    new_tournament = Tournament(
        name = tournament_name,
        players = sample(load_players.players, 16)
    )
    tournaments.append(new_tournament)

    new_tournament.generate_new_round().play_matches()
    new_tournament.generate_new_round().play_matches()
    new_tournament.generate_new_round().play_matches()
    
    load_players.save()
    load_tournaments.save()

    # load_players = PlayerManager()
    
    # tournament80 = Tournament(
    #     name='tournament 86533',
    #     place='Marseille',
    #     number_of_rounds=5,
    #     players=sample(load_players.players, 12),
    #     description='le premier tournois du nouvel an'
    # )
    
    # print_tournament(tournament80)
    
    # roundxyz = tournament80.generate_new_round()

    # roundxyz.play_matches()

    # print_round(roundxyz)

    # print_tournament(tournament80)

    # roundxyz_2 = tournament80.generate_new_round()

    # roundxyz_2.play_matches()

    # print_round(roundxyz_2)

    # print_tournament(tournament80)

    # print_players(load_players.players)

    # tournament90 = Tournament(
    #     name='tournament 2475957', 
    #     place='Paris',
    #     number_of_rounds=5,
    #     players=sample(load_players.players, 10), 
    #     description='le deuxieme tournois du nouvel an'
    #     )
    
    # print_tournament(tournament90)
    
    # roundabc = tournament90.generate_new_round()

    # roundabc.play_matches()

    # print_round(roundabc)

    # print_tournament(tournament90)

    # roundabc_2 = tournament90.generate_new_round()

    # roundabc_2.play_matches()

    # print_round(roundabc_2)

    # print_tournament(tournament90)

    # print_players(load_players.players)

if __name__ == '__main__':
    main()