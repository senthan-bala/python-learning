import turtle
from random import choice

teams = ["Griffindor", "Slitherin", "Hufflepuff", "Ravenclaw"]
players = ["harry", "hermione", "sirius", "peter", "ron", "neville", "ginny", "james"]
team_a = []
team_b = []


def team_chooser_b():
    player_b = choice(players)
    team_b.append(player_b)
    players.remove(player_b)


def team_chooser_a():
    player_a = choice(players)
    team_a.append(player_a)
    players.remove(player_a)


while len(players) > 0:
    team_chooser_a()
    if len(players) == 0:
        break
    team_chooser_b()


team_names_a = choice(teams)
teams.remove(team_names_a)
team_names_b = choice(teams)
teams.remove(team_names_b)

print(team_names_a, ":", team_a)
print(team_names_b, ":", team_b)
