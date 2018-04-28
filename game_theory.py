"""
#TODO: create interface for selecting AI's (terminal)
+ each AI should be a separate class
+ determine how to have AI's communicate with each other
+ need a score board/record-keeping system
+ store each class in a separate file
"""
import json
from game_manager import game_manager
from random import randint
from pprint import pprint
# For guide to Python with JSON, see http://docs.python-guide.org/en/latest/scenarios/json/
name = "random_v_random" #TODO: will later be determined by which AI's are engaged, hard-coded for now
json_manager = game_manager(name)

#"Game" Loop
loops = int(input("How many rounds would you like to start?"))

for i in range(0, loops):
    # generate random booleans
    rand1 = randint(1,4)
    rand2 = randint(1,4)
    if rand1 % 2 == 0:
        val1 = True
    else:
        val1 = False

    if rand2 % 2 == 0:
        val2 = True
    else:
        val2 = False

    game_results = [val1, val2]
    data = json_manager.get_data()
    data["game_rounds"] += 1
    data["game_outcomes"].append(game_results)

    json_manager.write_to_file(data)
pprint(json_manager.get_data())