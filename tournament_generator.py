from time import sleep

def num_of_team_validation(temp_num):
    """validate user input for the total number of teams, assume to be even int"""
    while True:
        if temp_num < 2:
            print("The minimum number of teams is 2, try again.")
            temp_num = int(input("Enter the number of teams in the tournament: "))
        
        else:
            return temp_num
            

def team_name_validation(temp_name, num):
    """validate user input for the name of a team"""
    temp_name = temp_name.strip(" ")
    while True:
        if len(temp_name) < 2:
            print("Team names must have at least 2 characters, try again.")
            temp_name = input(f"Enter the name for team #{num + 1}: ")
            temp_name = temp_name.strip(" ")
        
        elif len(temp_name.split(" ")) > 2:
            print("Team names may have at most 2 words, try again.")
            temp_name = input(f"Enter the name for team #{num + 1}: ")
            temp_name = temp_name.strip(" ")
        
        else:
            return temp_name


def num_of_game_validation(temp_num_of_game, num_of_team):
    """validate user input for number of game played by each team during regular season"""
    while True: 
        if temp_num_of_game < (num_of_team - 1):
            print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
            temp_num_of_game = int(input("Enter the number of games played by each team: "))

        else:
            return temp_num_of_game


def team_win_input_validation(temp_win, name, num_of_game):
    """validate user input for games wined by each team"""
    while True:
        if temp_win < 0:
            print("The minimum number of wins is 0, try again.")
            temp_win = int(input(f"Enter the number of wins Team {name} had: "))
        
        elif temp_win > num_of_game:
            print(f"The maximum number of wins is {num_of_game}, try again.")
            temp_win = int(input(f"Enter the number of wins Team {name} had: "))
        
        else: 
            return temp_win


def sort_method(tup):
    """ a function to e used as a sorting key"""
    return tup[1]


temp_num = int(input("Enter the number of teams in the tournament: "))
num_of_team = num_of_team_validation(temp_num)


team_names = []

for num in range(num_of_team):
    temp_name = input(f"Enter the name for team #{num + 1}: ")
    team_name = team_name_validation(temp_name, num)
    team_names.append(team_name)


temp_num_of_game = int(input("Enter the number of games played by each team: "))
num_of_game = num_of_game_validation(temp_num_of_game, num_of_team)


team_stats = []

for name in team_names:
    temp_win = int(input(f"Enter the number of wins Team {name} had: "))
    win = team_win_input_validation(temp_win, name, num_of_game)
    team_stats.append((name, win))


reverse_team_stats = sorted(team_stats, reverse=True, key = sort_method)
team_stats = sorted(team_stats, key = sort_method)

print("Generating the games to be played in the first round of the tournament...")
sleep(1)


for index in range (len(team_stats)//2):
    if not team_stats[index] == reverse_team_stats[index]:
        print(f"Home: {team_stats[index][0]} VS Away: {reverse_team_stats[index][0]}")
        
    else: 
        break

