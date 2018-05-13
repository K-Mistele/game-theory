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


