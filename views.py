from abc import ABC, abstractmethod

def print_tournament(obj):
    print("-" * 80)
    print("Listing all tournaments")
    for obj in tournaments:
        print(f"Tournament: {obj.name}    Location: {obj.place}    Start Date: {obj.start_date}")
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
    pass

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

class CreatePlayerView():
    def input_result(self):
        return input("Please ")

    
class ReportMenuView(MenuView):    
    def prompt_options(self):
        print(
            "Please choose an option:\n"
            "0: Exit menu\n"
            "1: Display all players\n"
            "2: Display tournament details (name, date, and place)\n"
            "3: Display tournament players\n"
            "4: Display tournament rounds\n"
            "5: Display ranking\n"
        )

    def all_players(self, players):
        print("Listing all players")
        print("-" * 80)
        for obj in players:
            f_name = obj.first_name
            l_name = obj.last_name
            dob = obj.dob
            id = obj.identifiant
            print(f"{f_name} {l_name}\n{dob} {id}") 
            #print(f"Matches played: {matches} Total score: {score}") 
            #print(f"Tournaments played in: {tournaments}")
        print("-" * 80)

    def choose_tournament(self, tournaments, aspect):
        print(f"\nDisplay {aspect} for which tournament?")
        for index, tournament in enumerate(tournaments):
            print(f"{index}: {tournament.name}")
        return input("Your choice: ")

    def tournament_details(self, tournament):
        print(f"\n\nDisplaying details for {tournament.name}\n")
        print(f"This tournament started on {tournament.start_date} and took place at {tournament.place}\n\n")

    def tournament_players(self, tournament):
        print(f"\n\nDisplaying players for {tournament.name}\n")
        for obj in tournament.players:
            print(f"{obj.first_name} {obj.last_name}\n")

    def tournament_rounds(self, tournament):
        print(f"\n\nDisplaying rounds for {tournament.name}\n")
        for obj in tournament.rounds:
            print("-" * 80)
            print(f"Round: {obj.name}    Date: {obj.start_date}")
            for item in obj.matches:
                print(f"\n{item[0][0].first_name} {item[0][0].last_name} {item[0][1]}")
                print(f"{item[1][0].first_name} {item[1][0].last_name} {item[1][1]}")
        print("-" * 80)

