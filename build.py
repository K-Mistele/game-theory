import glob
import os
import importlib
import json as JSON

class build:

    def __init__(self):

        # put instance of each AI in list
        self.AIs = []

        # build JSON data on AIs
        self.build_AI_data()

        #clear olf build data
        self.clear_old_build()

        #prompt to delete or keep old scores and games
        self.prompt_delete_existing_scores()

        print("Build Complete.")

    def build_AI_data(self):
        os.chdir("AI")
        for file in glob.glob("*.py"):
            AI_module = importlib.import_module(f"AI.{file[:-3]}")
            AI_class = getattr(AI_module, f"{file[:-3]}")
            AI = AI_class()
            self.AIs.append(AI)
        os.chdir("..")
        # build data
        build_data = {}

        # + create dictionary for each AI with name, gender, and behavior
        for AI in self.AIs:
            build_data[f"{AI.name}"] = {"name": AI.name,
                                        "gender": AI.gender,
                                        "behavior": AI.behavior_string}
        # + dump that data to a json file
        with open("json/build_data.json", "w") as build_file:
            JSON.dump(build_data, build_file)

    def clear_old_build(self):
        os.chdir("json")
        for file in glob.glob(".json"):
            if file == "build_data.json":
                os.remove(file)
        os.chdir("..")

    def prompt_delete_existing_scores(self):
        clear_game_data = input("Clear game data?  ")
        clear_scores = input("Clear all scores?  ")

        if clear_game_data:
            # clear past games
            os.chdir("json/games")
            for file in glob.glob(".json"):
                os.remove(file)

            #go back up two directories to main
            os.chdir("..")
            os.chdir("..")

        if clear_scores:
            # reset score data to empty
            os.chdir("json")
            empty = {}
            with open("scores.json", "w") as scores:
                JSON.dump(empty, scores)


new_build = build()
