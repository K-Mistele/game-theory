# import sub-managers
from json_manager import json_manager
from scores_manager import scores_manager

#import modules
import glob
import os
import json as JSON

class game_manager:
    def __init__(self):
        self.select_AIs()
        self.json_manager = json_manager(f"{self.first_AI.name}_v_{self.second_AI.name}")
        self.scores_manager = scores_manager(self.first_AI, self.second_AI)
        self.available_AIs = []

        #get points from decision matrix
        with open("decision_matrix.json", "r") as json_file:
            data = JSON.load(json_file)
            self.points = data

    def print_AIs(self):
        print("Available AI's: ")
        os.chdir("AI")
        for file in glob.glob("*.py"):
            print(file[:-3])
            self.available_AIs.append(file[:-3])
        os.chdir("..")


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
        while True:
            first_AI = input("Please select an AI to run:  ")
            if first_AI in self.available_AIs:

                #import class for AI based on name
                AI_module = __import__(first_AI)
                AI_class = getattr(AI_module, first_AI)
                self.first_AI = AI_class()
                self.first_AI_path = f"{self.first_AI}.py"
                break
            else:
                continue
        while True:
            second_AI = input("Please select an AI for it to compete with:  ")
            if second_AI in self.available_AIs:

                # import class for AI based on name
                AI_module = __import__(second_AI)
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
            outcome_1 = 300 # outcome state for 2nd AI victory
            outcome_2 = 400
        elif results == ["cooperate", "compete"]:
            outcome_1 = 400 # outcome state for 1st AI victory
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
                game_results = [self.first_AI.take_turn(),
                                self.second_AI.take_turn()]

            # parse game results into outcome code
            parsed_results = self.parse_game_results((game_results))

            #determine score for each AI
            first_AI_outcome = parsed_results[0]
            second_AI_outcome = parsed_results[1]

            data = self.json_manager.get_data()
            data["game_rounds"] += 1
            data["game_outcomes"].append(game_results)
            self.json_manager.write_to_file(data)


