class decision_matrix:

    def __init__(self, probabilities=((1,0),(1,0))):
        self.matrix = {
            "cooperate": {
                "cooperate": probabilities[0][0],
                "compete": probabilities[0][1]
            },
            "compete": {
                "cooperate": probabilities[1][0],
                "compete": probabilities[1][1]
            }
        }
    def get_decision(self, state):
        if state == "cooperate" or state == "compete":
            for key in self.matrix[state]:
                #iterate through keys and whichever one has a probability of 1 is returned
                if self.matrix[state][key] == 1:
                    return key
        else:
            #error state
            return "cooperate"


