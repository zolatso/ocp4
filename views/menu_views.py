from abc import ABC, abstractmethod


class MenuView(ABC):
    @abstractmethod
    def prompt_options(self):
        pass

    def input_result(self):
        return input("Please enter an option: ")

    def invalid_option(self, option):
        print(
            f"\nOption {option} is invalid, please choose one of the numbers listed\n"
        )

    def invalid_input(self):
        print("\nPlease enter a number\n")


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


class CreatePlayerView:
    def input(self, aspect):
        return input(f"Please enter the player's {aspect}: ")

    def error_msg(self):
        print("Something wrong with the input")

    def success_msg(self, player):
        print(
            f"Player {player.first_name} {player.last_name} has been successfully created"
        )


class CreateTournamentView:
    def input(self, aspect):
        return input(f"Please enter the tournament's {aspect}: ")

    def error_msg(self, error):
        print(f"Input error: {error}")

    def success_msg(self):
        print("The tournament has been successfully created and saved")

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
        )

    def all_players(self, players):
        print("\n\n")
        print("Listing all players by alphabetical order")
        print("-" * 80)
        for obj in players:
            f_name = obj.first_name
            l_name = obj.last_name
            dob = obj.dob
            id = obj.identifiant
            spaces = 50 - (len(l_name) + len(f_name))
            gap = " " * spaces
            print(f"{l_name}, {f_name}{gap}{dob}     {id}")
        print("\n\n")

    def choose_tournament(self, tournaments, aspect):
        print(f"\nDisplay {aspect} for which tournament?")
        for index, tournament in enumerate(tournaments):
            print(f"{index}: {tournament.name}")
        return input("Your choice: ")

    def tournament_display(self, tournament, aspect):
        if aspect == "details":
            print(f"\n\nDisplaying details for {tournament.name}\n")
            print(
                f"This tournament started on {tournament.start_date} and took place at {tournament.place}\n\n"
            )

        elif aspect == "players":
            print(f"\n\nDisplaying players for {tournament.name}\n")
            for player in sorted(
                tournament.players, key=lambda player: player.last_name
            ):
                print(f"{player.last_name}, {player.first_name}")
            print("\n\n")

        elif aspect == "rounds":

            print(f"\n\nDisplaying rounds for {tournament.name}\n")
            for obj in tournament.rounds:
                print("-" * 80)
                print(f"Round: {obj.name}    Date: {obj.start_date}")
                for item in obj.matches:
                    spaces_a = 40 - (
                        len(item[0][0].first_name) + len(item[0][0].last_name)
                    )
                    spaces_b = 40 - (
                        len(item[1][0].first_name) + len(item[1][0].last_name)
                    )
                    gap_a = " " * spaces_a
                    gap_b = " " * spaces_b
                    print(
                        f"\n{item[0][0].first_name} {item[0][0].last_name} {gap_a} {item[0][1]}"
                    )
                    print(
                        f"{item[1][0].first_name} {item[1][0].last_name} {gap_b} {item[1][1]}"
                    )
            print("-" * 80)


class TournamentMenuView(MenuView):
    def choose_tournament(self, tournaments):
        print("\nDisplaying list of all unfinished tournaments\n")
        for index, tournament in enumerate(tournaments):
            print(f"{index}: {tournament.name}")

        return input("\nWhich tournament do you want to work on: ")

    def prompt_options(self, tournament):
        print(f"What do you want to do on {tournament.name} ?:\n")
        print(
            "0: Exit menu\n"
            "1: Generate pairs for new round\n"
            "2: Input scores for current round\n"
        )

    def error_msg(self, error):
        print("\n")
        print(f"Input error: {error}")
        print("\n")

    def dislay_matches(self, round):
        for match in enumerate(round.matches):
            print(f"{match[0][0].first_name} {match[0][0].last_name} {match[0][1]}\n")
            print(f"{match[1][0].first_name} {match[1][0].last_name} {match[1][1]}\n")

    def successful_pair_generation(self, tournament, round):
        print("\n")
        print(f"Pairs successfully generated for {round.name} of {tournament.name}")
        for match in round.matches:
            player_a = match[0][0].first_name + " " + match[0][0].last_name
            player_b = match[1][0].first_name + " " + match[1][0].last_name
            print(f"{player_a} vs. {player_b}")
        print("\n")

    def successful_score_entry(self, tournament):
        print("\n")
        print(
            f"Scores successfully entered for Round {len(tournament.rounds)} of {tournament.name}"
        )
        print("\n")

    def input_scores(self, match, index):
        print(
            f"\nMatch {index + 1}\nPlayer 1: {match[0][0].first_name} {match[0][0].last_name} "
            f"\nPlayer 2: {match[1][0].first_name} {match[1][0].last_name}\n\n"
            f"Who won?\n"
            f"For Player 1, enter 1. For Player 2, enter 2. For a draw, enter 3.\n"
        )
        return input("Enter: ")
