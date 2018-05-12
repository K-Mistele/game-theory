# import sub-managers
from json_manager import json_manager
from scores_manager import scores_manager
import importlib

#import modules
import glob
import os
import inspect
import json as JSON
from pprint import pprint

class game_manager:
    def __init__(self):
        self.available_AIs = []
        self.select_AIs()
        self.json_manager = json_manager(f"{self.first_AI.name}_v_{self.second_AI.name}", self.first_AI, self.second_AI)
        self.scores_manager = scores_manager(self.first_AI, self.second_AI)


        #get points from decision matrix
        with open("json/decision_matrix.json", "r") as json_file:
            data = JSON.load(json_file)
            self.points = data

    def print_AIs(self):
        with open("json/build_data.json", "r") as build_file:
            build_data = JSON.load(build_file)
        self.available_AIs = []

        print("Available AI's: ")
        for key in build_data:
            self.available_AIs.append(build_data[key]["name"]) # add AI to availabe AI's
            print(f"    {build_data[key]['name']} ({build_data[key]['gender']})\n      {build_data[key]['behavior']}\n")
        # os.chdir("AI")
        # for file in glob.glob("*.py"):
        #     print(file[:-3])
        #     self.available_AIs.append(file[:-3])
        # os.chdir("..")


    def get_loops(self):
        while True:
            try:
                loops = int(input("How many games would you like to run?"))
                break
            except:
                continue
        self.num_loops = loops
        return loops

    def select_AIs(self):
        self.print_AIs()
        print("(Note: AI's currently are not able to compete with themselves.)")
        while True:
            first_AI = input("Please select a valid AI to run:  ")
            if first_AI in self.available_AIs:

                #import class for AI based on name

                # os.chdir("AI")
                # os.system("cd")

                AI_module = importlib.import_module(f"AI.{first_AI}")
                AI_class = getattr(AI_module, first_AI)
                pprint(AI_module)
                pprint(AI_class)
                self.first_AI = AI_class()
                break
            else:
                continue
        while True:
            second_AI = input("Please select a valid AI for it to compete with:  ")
            if second_AI in self.available_AIs and second_AI != self.first_AI.name:

                # import class for AI based on name
                AI_module =importlib.import_module(f"AI.{second_AI}")
                AI_class = getattr(AI_module, second_AI)
                self.second_AI = AI_class()
                break
            else:
                continue

    def parse_game_results(self, results):
        #NOTE: game_results should be a list of two items where each is either "cooperate" or "compete"
        if results == ["cooperate", "cooperate"]:
            outcome_1 = 100 # outcome state 1 for cooperation
            outcome_2 = 100
        elif results == ["compete", "compete"]:
            outcome_1 = 200 # outcome state 2 for competition
            outcome_2 = 200
        elif results == ["compete", "cooperate"]:
            outcome_1 = 300 # outcome state for 1st AI victory
            outcome_2 = 400
        elif results == ["cooperate", "compete"]:
            outcome_1 = 400 # outcome state for 2nd AI victory
            outcome_2 = 300
        else:
            outcome_1 = 999 # error state
            outcome_2 = 999
        return [outcome_1, outcome_2]

    def game_loop(self):

        for i in range(0, self.get_loops()):
            # if first turn,each AI will exercise first turn behavior

            if i == 0:
                game_results = [self.first_AI.first_turn(),
                                self.second_AI.first_turn()]


            # otherwise, each AI will exercise normal behavior
            else:
                # data from past games to make decisions beased off of.

                old_data = self.json_manager.get_data()
                game_data = old_data["game_outcomes"]
                game_results = [self.first_AI.take_turn(game_data),
                                self.second_AI.take_turn([item.reverse() for item in game_data])] # give AI data with its own responses first
                #TODO: reverse each item in list not the list itself!!!

            # parse game results into outcome code
            parsed_results = self.parse_game_results(game_results)

            #determine score for each AI
            self.first_AI.outcome = parsed_results[0]
            self.second_AI.outcome = parsed_results[1]

            # get data
            data = self.json_manager.get_data()

            # upate data with info from game round
            data["game_rounds"] += 1
            data["game_outcomes"].append(game_results)

            # game meta data
            if parsed_results == [100, 100]: # if both cooperated
                data["game_meta_data"]["cooperated"] += 1
            elif parsed_results == [200, 200]:
                data["game_meta_data"]["competed"] += 1
            elif parsed_results == [400, 300]:
                data["game_meta_data"][f"{self.first_AI.name} won"] += 1
            elif parsed_results == [300, 400]:
                data["game_meta_data"][f"{self.second_AI.name} won"] += 1

            #update local scores
            data["scores"][self.first_AI.name] += self.points[f"{parsed_results[0]}"]
            data["scores"][self.second_AI.name] += self.points[f"{parsed_results[1]}"]

            #update global scores
            self.scores_manager.update_global_scores(self.points[f"{parsed_results[0]}"], self.points[f"{parsed_results[1]}"])

            # save data to game file
            self.json_manager.write_to_file(data)
