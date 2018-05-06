#import modules
import json as JSON
from pprint import pprint


import os
# class for writing to/from files for communication between AI's
class json_manager:
    def __init__(self, fname):
        self.fname = f"{fname}.json"

        # open template and storage file
        with open("game_template.json", "r") as template:
            self.template_data = JSON.load(template)

        if os.path.isfile(self.fname):
            with open(self.fname, "r+") as new_file:
                self.file_data = JSON.load(new_file)
        else:
            with open(self.fname, "w") as new_file:
                JSON.dump(self.template_data, new_file)




    def __repr__(self):
        with open(self.fname, "r") as json_file:
            pprint(JSON.load(json_file)) # print all data in file so far


    #method for encoding Python data to JSON
    # def encode_json(self, to_encode):
    #     json_string = JSON.dump(to_encode)
    #     return json_string

    #method for decoding JSON to Python
    # def decode_json(self, to_decode):
    #     python_data = JSON.load(to_decode)
    #     return python_data

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

    def process_data(self, AI_1, AI_2, data):
        if AI_1.goes_first == True and AI_2.goes_first == False:
            return [data, data] # data for first AI, and for second
        elif AI_1.goes_first == False and AI_2.goes_first == True:
            data2 = data[:]
            for game in data2:
                game.reverse() # reverse order
            return [data2, data]
        else: # if AI's can't agree which goes first, assign order
            AI_1.goes_first = True
            AI_2.goes_first = False
            return [data, data]

    # display available AI's

