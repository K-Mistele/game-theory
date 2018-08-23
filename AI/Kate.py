class Kate:

    behavior_string = "Two-tits-for-tat AI"
    gender = "female"
    name = "Kate"

    def __init__(self):
        self.tat_counter = 0

    def first_turn(self):
        return "cooperate"

    def take_turn(self, data=()):
        last_two_turns  = [data[-1][1], data[-2][1]] # opponent's last two moves

        # if opponent has competed within past two moves, compete; otherwise cooperate
        # NOTE: effectively defects twice for each defection by the opponent. Multiple defections in a row by the opponent
        # NOTE: will lead to defection by Kate until opponent ceases defecting, at which point Kate will defect twice
        if "compete" in last_two_turns:
            return "compete"
        else:
            return "cooperate"