def print_tournament(obj):
    print("-" * 80)
    print("Printing Tournament")
    print("-" * 80)
    print(f"Tournament: {obj.name}    Location: {obj.place}    Date: {obj.start_date}")
    print("-" * 80)
    print(f"List of players and their overall scores in the tournament")
    for item in obj.list_of_players:
        f_name = item.player.first_name
        l_name = item.player.last_name
        length_of_name = 70 - len(f_name + l_name)
        spaces = " " * length_of_name
        print(f"{f_name} {l_name} {spaces} {item.score_in_tournament}")

def print_round(obj):
    print("-" * 80)
    print("Printing Round")
    print("-" * 80)
    print(f"Tournament: {obj.tournament.name}    Round: {obj.name}    Date: {obj.start_date}")
    print("-" * 80)
    print(f"List of matches and scores")
    for item in obj.list_of_matches:
        #length_of_name = 70 - len(item[0].first_name + item[0].last_name)
        #spaces = " " * length_of_name
        #print(f"{item[0].first_name} {item[0].last_name} {spaces} {item[1]}")
        print(f"Match")
        print(f"{item.playerA.player.first_name} {item.playerA.player.last_name} {item.playerA_score}")
        print(f"{item.playerB.player.first_name} {item.playerB.player.last_name} {item.playerB_score}")

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
        print(f"Matches played: {matches} Total score: {score}") 
        print(f"Tournaments played in: {tournaments}")
        print("-" * 80)   