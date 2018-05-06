class Steve:

    behavior_string = "Tit-for-Tat AI. In memoriam Steve Jobs."
    gender = "male"
    name = "Steve"

    def first_turn(self):
        return "cooperate"

    def take_turn(self, data=()):
        if data[-1][1] == "compete": # if opponent competed last turn
            return "compete"
        else:
            return "cooperate"