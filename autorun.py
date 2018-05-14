"""
#AUTORUN

+ runs all available AI's against each other

+ does NOT do all possible combinations and permutations,
+ each AI only plays each other AI once.

+ select number of rounds at beginning of file
"""
# import manager
from managers.game_manager import game_manager

#import modules
from pprint import pprint
import json as JSON

# make sure user has created a build
user_input = input("Make sure to run >>python build.py<< before attempting to autorun games. Continue? (y/n)  ")
if user_input in "yes":
    pass
else:
    quit()

# get build data
with open("json/build_data.json", "r") as build:
    build_data = JSON.load(build)

# generate non-redundant yet exhaustive combinations of AIs
# NOTE: specifically designed so no AI will play itself, nor will it play any other AI twice.
primary_list = [key for key in build_data]
secondary_list = primary_list[:]

combinations = [(AI_1, AI_2) for AI_1 in primary_list for AI_2 in secondary_list
                if (AI_1 != AI_2 and primary_list.index(AI_1) > secondary_list.index(AI_2))]

#get number of loops to run
while True:
    try:
        loops = int(input("How many loops should each AI run?  "))
        break
    except:
        continue

# run games
print(combinations)
for combination in combinations:
    manager = game_manager(True, combination, loops)
    manager.game_loop()

#TODO: analyze data and global scores
