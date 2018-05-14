from classes.transition_matrix import transition_matrix
class George:

    behavior_string = "Competes until enemy starts consistently competing"
    gender = "male"
    name = "George"

    def first_turn(self):
        return "compete"

    def take_turn(self, data=()):
        try:
            last_three_games = [data[-1], data[-2], data[-3]]
        except:
            try:
                last_three_games = [data[-1], data[-2]]
            except:
                last_three_games = [data[-1]]

        if (last_three_games.count(["compete", "compete"]) +
            last_three_games.count(["cooperate", "compete"]) >= 2): # if opponent is competing
            return "cooperate"
        else:
            return "compete"
