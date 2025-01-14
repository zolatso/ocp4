import json
import os
import datetime

class Player:
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = datetime.datetime.strptime(dob, "%d/%m/%Y").date()


class Tournament:
    def __init__(self, name, place, start_date, end_date, number_of_rounds, current_round,
                list_of_rounds, list_of_players, description):
        self.name = name
        self.place = place
        self.start_date = start_date 
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.list_of_rounds = list_of_rounds
        self.list_of_players = list_of_players
        self.description = description


class Round:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date


class Match:
    def __init__(self, ):
        pass

def generate_random_pairs(list_of_players):
    

def generate_pairs(list_of_players):

def list_of_players():
    # This function takes the players json file and converts it into a list of player objects
    file_to_open = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/players/players.json')
    with open(file_to_open, 'r') as f:
        initial_list = json.load(f)
    converted_list = []
    for person in initial_list:
        converted_list.append(Player(person[0], person[1], person[2]))
    return converted_list

def main():
    players = list_of_players()
    print(players[10].last_name)


if __name__ == '__main__':
    main()

   