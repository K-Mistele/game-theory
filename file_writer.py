import json as JSON
from pprint import pprint
# class for writing to/from files for communication between AI's
class file_writer:
    def __init__(self, fname):
        self.fname = f"{fname}.json"

        # open template and storage file
        with open("game_template.json", "r") as template:
            self.template_data = JSON.load(template)
        with open(self.fname, "r") as new_file:
            self.file_data = JSON.load(new_file)

        # if file is empty, create a new one based off of template
        if "game_rounds" not in self.file_data:
            with open(self.fname, "w") as new_file:
                JSON.dump(self.template_data, new_file)

    def __repr__(self):
        with open(self.fname, "r") as json_file:
            pprint(JSON.load(json_file)) # print all data in file so far


    #method for encoding Python data to JSON
    def encode_json(self, to_encode):
        json_string = JSON.dumps(to_encode)
        return json_string

    #method for decoding JSON to Python
    def decode_json(self, to_decode):
        python_data = JSON.loads(to_decode)
        return python_data

    #method for writing to file
    def write_to_file(self, to_write, want_encoded=False):
        if want_encoded == True:
            with open(self.fname, "w+") as json_file:
                JSON.dump(self.encode_json(to_write), json_file)

    # getting all data in file
    def read_file(self):
        with open(self.fname, "r") as json_file:
            data = JSON.load(json_file)
            return data

    # get results of last game
    def get_last_game_results(self):
        data = self.read_file["game_outcomes"]
        last_game = data[len(data)-1]
        return last_game

