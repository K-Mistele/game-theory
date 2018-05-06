class George:

    behavior_string = "Competes until enemy starts consistently cooperating"
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

        if (last_three_games.count(["cooperate", "compete"]) +
            last_three_games.count(["compete", "cooperate"]) == len(last_three_games) ):
            return "cooperate"
        else:
            return "compete"