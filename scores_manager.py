#modules
import json as JSON
from pprint import pprint

class scores_manager():
    def __init__(self, first_AI, second_AI, data_path="scores.json"):
        self.data_path = data_path
        self.first_AI = first_AI
        self.second_AI = second_AI

