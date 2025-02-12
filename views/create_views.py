class CreateView:
    def error_msg(self, error):
        print("\n")
        print(f"Input error: {error}")
        print("\n")


class CreatePlayerView(CreateView):
    def input(self, aspect):
        return input(f"Please enter the player's {aspect}: ")

    def success_msg(self, player):
        print("\n")
        print(
            f"Player {player.first_name} {player.last_name} has been successfully created"
        )
        print("\n")


class CreateTournamentView(CreateView):
    def input(self, aspect):
        return input(f"Please enter the tournament's {aspect}: ")

    def success_msg(self):
        print("\n")
        print("The tournament has been successfully created and saved")
        print("\n")

    def choose_players(self, players):
        print("\n")
        for index, player in enumerate(players):
            print(f"{index}: {player.first_name} {player.last_name}")
        print("\nPlease choose all the players in the tournament.\n")
        return input("List the numbers separated by spaces:")
