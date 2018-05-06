"""
#TODO: create interface for selecting AI's (terminal)
+ each AI should be a separate class
+ determine how to have AI's communicate with each other
+ need a score board/record-keeping system
+ store each class in a separate file
"""
from game_manager import game_manager
from random import randint
from pprint import pprint

# For guide to Python with JSON, see http://docs.python-guide.org/en/latest/scenarios/json/
name = "random_v_random" #TODO: will later be determined by which AI's are engaged, hard-coded for now
manager = game_manager()

#"Game" Loop
manager.game_loop()

pprint(manager.json_manager.get_data())
print("Global Scores:")
pprint(manager.scores_manager.get_global_scores())

