import json
import pygame

filename = "user_settings.txt"
myfile = open(filename, mode='w',encoding='Latin-1')
player1 = {
    'playerName': "Donald Trump",
    'Score': 345,
    'awards': ["OR", "NV", "NY"]

}

player2 = {
    'playerName': "Clinton Hillary",
    'Score': 346,
    'awards': ["WT", "TX", "MI"]

}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

# -------- SAVE by JSON------
json.dump(myplayers, myfile)
myfile.close()

# ------------------Load by JSON---------------
myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)

for user in json_data:
    print("Player Name is: " + str(user['playerName']))
    print("Player Score is:" + str(user['Score']))
    print("Player Award N1: " + str(user['awards'][0]))
    print("Player Award N2: " + str(user['awards'][1]))
    print("Player Award N3: " + str(user['awards'][2]))
    print("-------------------\n\n")
