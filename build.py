import glob
import os
import importlib
import json as JSON

class build:

    def __init__(self):

        # put instance of each AI in list
        self.AIs = []
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
        print("Build Complete.")

new_build = build()
