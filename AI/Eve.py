class Eve():

    behavior_string = "Very cooperative, and has faith in other people"
    gender = "female"
    name = "Eve"

    def first_turn(self):
        return "cooperate"

    def take_turn(self, data):

        # behavior if the other AI is being very uncooperative
        if (["compete", "cooperate"] not in last_three_games and
            ["cooperate", "compete"] not in last_three_games and
            ["compete", "compete"]):
            return "cooperate"
        else:
            return "compete"



