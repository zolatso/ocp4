from abc import ABC, abstractmethod

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
            "2: Add games/rounds to tournament\n"
            "3: Create player\n"
            "4: Show reports\n"
        )
    
    def invalid_option(self, option):
        print(f"Option {option} is invalid, please choose a number between 0 and 4")


class CreatePlayerView():
    def input(self, aspect):
        return input(f"Please enter the player's {aspect}: ")
    
    def error_msg(self):
        print("Something wrong with the input")


class CreateTournamentView():
    def input(self, aspect):
        return input(f"Please enter the tournament's {aspect}: ")
    
    def error_msg(self, error):
        print(f"Input error: {error}")
    
    def success_msg(self):
        print(f"The tournament has been successfully created and saved")

    def choose_players(self, players):
        for index, player in enumerate(players):
            print(f"{index}: {player.first_name} {player.last_name}")
        print("Please choose all the players in the tournament.\n")
        return input("List the numbers separated by spaces:")

    
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

    def tournament_display(self, tournament, aspect):
        if aspect == 'details':
            print(f"\n\nDisplaying details for {tournament.name}\n")
            print(f"This tournament started on {tournament.start_date} and took place at {tournament.place}\n\n")

        elif aspect == 'players':
            print(f"\n\nDisplaying players for {tournament.name}\n")
            for obj in tournament.players:
                print(f"{obj.first_name} {obj.last_name}\n")

        elif aspect == 'rounds':
            print(f"\n\nDisplaying rounds for {tournament.name}\n")
            for obj in tournament.rounds:
                print("-" * 80)
                print(f"Round: {obj.name}    Date: {obj.start_date}")
                for item in obj.matches:
                    print(f"\n{item[0][0].first_name} {item[0][0].last_name} {item[0][1]}")
                    print(f"{item[1][0].first_name} {item[1][0].last_name} {item[1][1]}")
            print("-" * 80)

class TournamentMenuView(MenuView):
    def choose_tournament(self, tournaments):
        for index, tournament in enumerate(tournaments):
            print(f"{index}: {tournament.name}")
        print(f"\n Displaying list of all unfinished tournaments")
        return input("Which tournament do you want to work on: ")
    
    def prompt_options(self, tournament):
        print(f"What do you want to do on {tournament.name} ?:\n")
        print(
            "0: Exit menu\n"
            "1: Generate pairs for new round\n"
            "2: Input scores for current round\n"
        )

    def error_msg(self, error):
        print(f"Input error: {error}")
    
    def dislay_matches(self, round):
        for match in enumerate(round.matches):
            print(f"{match[0][0].first_name} {match[0][0].last_name} {match[0][1]}\n")
            print(f"{match[0][0].first_name} {match[0][0].last_name} {match[0][1]}\n")

    def successful_pair_generation(self, tournament):
        print(f"\n")
        print(f"Pairs successfully generated for Round {len(tournament.rounds)} of {tournament.name}")
        print(f"\n")

    def successful_score_entry(self, tournament):
        print(f"\n")
        print(f"Scores successfully entered for Round {len(tournament.rounds)} of {tournament.name}")
        print(f"\n")

    def input_scores(self, match, index):
        print(
            f"\nMatch {index + 1}\nPlayer 1: {match[0][0].first_name} {match[0][0].last_name} "
            f"\nPlayer 2: {match[1][0].first_name} {match[1][0].last_name}\n\n"
            f"Who won?\n"
            f"For Player 1, enter 1. For Player 2, enter 2. For a draw, enter 3.\n"
            )
        return input("Enter: ")
