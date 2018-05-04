from json_manager import json_manager
import glob
import os

class game_manager:
    def __init__(self):
        self.json_manager = json_manager


    def print_AIs(self):
        os.chdir("AI")
        for file in glob.glob("*.py"):
            print(file[:-3])
        loops = int(input("How many rounds would you like to start?"))
        os.chdir("..")