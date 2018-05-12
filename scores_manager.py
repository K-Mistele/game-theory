#modules
import json as JSON
from pprint import pprint

class scores_manager():
    def __init__(self, first_AI, second_AI, data_path="scores.json"):
        self.data_path = f"json/{data_path}"
        self.first_AI = first_AI
        self.second_AI = second_AI

    def update_global_scores(self, score1, score2):
        # get existing global_scores
        with open(self.data_path, "r") as scores:
            self.global_scores = JSON.load(scores)

        # making sure there is an entry for each AI in global scores, and if not then it's creating one
        self.global_scores[self.first_AI.name] = self.global_scores.get(self.first_AI.name, {"rounds": 0,
                                                                                             "total_score": 0,
                                                                                             "average_score": 0})
        self.global_scores[self.second_AI.name] = self.global_scores.get(self.second_AI.name, {"rounds": 0,
                                                                                             "total_score": 0,
                                                                                             "average_score": 0})



        # update average score for each AI
        self.global_scores[self.first_AI.name]["average_score"] = self.recalculate_average_score(
            self.global_scores[self.first_AI.name]["average_score"],
            self.global_scores[self.first_AI.name]["rounds"],
            score1
            )
        self.global_scores[self.second_AI.name]["average_score"] = self.recalculate_average_score(
            self.global_scores[self.second_AI.name]["average_score"],
            self.global_scores[self.second_AI.name]["rounds"],
            score2
        )

        # update rounds and total score for each AI
        self.global_scores[self.first_AI.name]["rounds"] += 1
        self.global_scores[self.first_AI.name]["total_score"] += score1

        self.global_scores[self.second_AI.name]["rounds"] += 1
        self.global_scores[self.second_AI.name]["total_score"] += score2

        # save new global scores data
        with open(self.data_path, "w") as scores_file:
            JSON.dump(self.global_scores, scores_file)

    def recalculate_average_score(self, avg, rounds, new_score):
        exp_avg = avg * rounds # epand average: the average times number of rounds
        exp_avg += new_score # add new score to average
        exp_avg /= (rounds + 1) # re-calculate average
        return exp_avg

    def get_global_scores(self):
        with open(self.data_path, "r") as scores_file:
            return JSON.load(scores_file)


