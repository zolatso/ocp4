from abc import ABC, abstractmethod

def print_tournament(obj):
    print("-" * 80)
    print("Printing Tournament")
    print("-" * 80)
    print(f"Tournament: {obj.name}    Location: {obj.place}    Date: {obj.start_date}")
    print("-" * 80)
    print(f"List of players and their overall scores in the tournament")
    for item in obj.players:
        f_name = item.first_name
        l_name = item.last_name
        length_of_name = 70 - len(f_name + l_name)
        spaces = " " * length_of_name
        #print(f"{f_name} {l_name} {spaces} {item.score_in_tournament(obj)}")
        print(f"{f_name} {l_name}")

def print_round(obj):
    print("-" * 80)
    print("Printing Round")
    print("-" * 80)
    #print(f"Tournament: {obj.tournament.name}    Round: {obj.name}    Date: {obj.start_date}")
    print(f"Round: {obj.name}    Date: {obj.start_date}")
    print("-" * 80)
    print(f"List of matches and scores")
    for item in obj.matches:
        #length_of_name = 70 - len(item[0].first_name + item[0].last_name)
        #spaces = " " * length_of_name
        #print(f"{item[0].first_name} {item[0].last_name} {spaces} {item[1]}")
        print(f"Match")
        print(f"{item[0][0].first_name} {item[0][0].last_name} {item[0][1]}")
        print(f"{item[1][0].first_name} {item[1][0].last_name} {item[1][1]}")

def print_players(players):
    print("-" * 80)
    print("Printing Players")
    print("-" * 80)
    for item in players:
        f_name = item.first_name
        l_name = item.last_name
        dob = item.dob
        matches = item.matches_played
        score = item.total_score
        if item.tournaments:
            tournaments = []
            for item in item.tournaments:
                tournaments.append(item.name)
        else: 
            tournaments = "None"
        
        print("-" * 80)
        print(f"Player: {f_name} {l_name} {dob}") 
        #print(f"Matches played: {matches} Total score: {score}") 
        #print(f"Tournaments played in: {tournaments}")
        print("-" * 80)

class MenuView(ABC):
    @abstractmethod
    def prompt_options(self):
        pass

    def input_result(self):
        return input("Please enter an option: ")

class MainMenuView(MenuView):
    def prompt_options(self):
        print(
            "Please choose an option:\n"
            "0: Exit menu\n"
            "1: Create tournament\n"
            "2: Load tournament\n"
            "3: Create player\n"
            "4: Show reports\n"
        )
    
    def invalid_option(self, option):
        print(f"Option {option} is invalid, please choose a number between 0 and 4")
    
class ReportMenuView(MenuView):
    def choose_tournament(self, tournaments):
        print("Please choose a tournament among those:")
        for index, tournament in enumerate(tournaments):
            print(f"{index}: {tournament}")
        return input("Your choice: ")

    def prompt_options(self):
        print(
            "Please choose an option:\n"
            "0: Exit menu\n"
            "1: Display all players\n"
            "2: Display all tournament\n"
            "3: Display tournament details (name and date)\n"
            "4: Display tournament players\n"
            "5: Display tournament rounds\n"
        )