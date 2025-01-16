def print_tournament(obj):
    print("-" * 80)
    print(f"Tournament: {obj.name}    Location: {obj.place}    Date: {obj.start_date}")
    print("-" * 80)
    print(f"List of players and their overall scores in the tournament")
    for item in obj.list_of_players:
        length_of_name = 70 - len(item[0].first_name + item[0].last_name)
        spaces = " " * length_of_name
        print(f"{item[0].first_name} {item[0].last_name} {spaces} {item[1]}")