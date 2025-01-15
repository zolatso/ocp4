import json
import os
import datetime

class Player:
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = datetime.datetime.strptime(dob, "%d/%m/%Y").date()


class Tournament:
    def __init__(self, name, place, number_of_rounds, list_of_players,
                description):
        self.name = name
        self.place = place
        self.start_date = datetime.datetime.now().date()
        self.number_of_rounds = 4 if number_of_rounds is 0 else number_of_rounds
        self.current_round = 0
        self.list_of_players = list_of_players
        self.description = description

    def generate_new_round(self):
        


class Round:
    def __init__(self, name, start_date):
        self.name = name
        self.start_date = datetime.datetime.now().date()


class Match:
    def __init__(self, ):
        pass


    



def extract_players(n):
    # This function takes the players json file and converts it into a list of player objects
    file_to_open = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/players/players.json')
    with open(file_to_open, 'r') as f:
        initial_list = json.load(f)
    converted_list = []
    for i in range(5):
        converted_list.append(Player(initial_list[i][0], initial_list[i][1], initial_list[i][2]))
    return converted_list

def main():
    tournament80 = Tournament('egg', 'London', 5, extract_players(6), 'this is going to be a good tourny')
    print(tournament80.list_of_players[5].first_name)


if __name__ == '__main__':
    main()

   