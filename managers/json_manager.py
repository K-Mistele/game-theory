#import modules
import json as JSON
from pprint import pprint


import os
# class for writing to/from files for communication between AI's
class json_manager:
    def __init__(self, fname, first_AI, second_AI):
        if not os.path.exists("json/games"): os.makedirs("json/games")
        self.fname = f"json/games/{fname}.json"

        # open template and storage file
        with open("json/game_template.json", "r") as template:
            self.template_data = JSON.load(template)

        # if creating file from template, add relevant attributes
        if os.path.isfile(self.fname):
            with open(self.fname, "r+") as new_file:
                self.file_data = JSON.load(new_file)
        else:
            self.update_template_data_with_AIs(first_AI, second_AI)
            with open(self.fname, "w") as new_file:
                JSON.dump(self.template_data, new_file)

    def __repr__(self):
        with open(self.fname, "r") as json_file:
            pprint(JSON.load(json_file)) # print all data in file so far

    #method for writing to file
    def write_to_file(self, to_write, want_encoded=True):
        if want_encoded == True:
            with open(self.fname, "w+") as json_file:
                JSON.dump(to_write, json_file)
        else:
            with open(self.fname, "w+") as json_file:
                JSON.dump(to_write, json_file)

    # getting all data in file
    def get_data(self):
        with open(self.fname, "r") as json_file:
            data = JSON.load(json_file)
            return data

    # get results of last game
    def get_last_game_results(self):

        data = self.get_data()["game_outcomes"]
        last_game = data[len(data)-1]
        return last_game

    def update_template_data_with_AIs(self, first_AI, second_AI):
        self.template_data["game_meta_data"] = {
            "cooperated": 0,
            "competed": 0,
            f"{first_AI.name} won": 0,
            f"{second_AI.name} won": 0
        }
        self.template_data["scores"] = {
            f"{first_AI.name}": 0,
            f"{second_AI.name}": 0
        }
