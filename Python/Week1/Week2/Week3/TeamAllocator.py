# This program will allocate tean randomly from a list of 
# 1. Import  the random module
# 2. Create a list of every Genius
# 3. Use the random module to randomly shuffle the list
# 4. Loop through the list and display each teams
#5. Using an if statemant to see if the user is happy with their team
# If not, it will shuffle again. If so, the program terminates

import random

# Create a list of players stored in the players variable
players = ["Semaj", "Joseph", "Tay",
            "Taqari", "Kriss", "Kauri",
            "Marchaun", "Joaquin", "Nahum",
            "Darren", "EJ", "Walter",
            "Carl", "Avery", "Xaivier",
            "Braylen", "Max", "Kenlan,"
            "Nishad", "JaDen", "Isaiah,"
            "Jamauri", "Kamari", "Jefferey"]

def PickTeams(players):     # Create our function
    random.shuffle(players) # Shuffle the list of players
    team1 = players[:len(players) // 2] # Put the 1st half of the players into the 1st team 
    teamCaptain1 = team1[random.randrange(0, 12)] # Randomly assign a tean captain

    print("TEAM 1:")
    print("Team 1 Captain: " + teamCaptain1)
    for player in team1:
        print(player)
team2 = players[len(players) // 2:] # Put the 2nd half of the players in the second team
teamCaptain2 = team2[random.randrange(0, 12)]

print("TEAM 2")
print("Team 2 Captain: " + teamCaptain2)
for player in team2:
    print(player)


PickTeams(players)
