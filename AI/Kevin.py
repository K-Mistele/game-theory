class Kevin:

    behavior_string = "Tit-for-two-tats AI"
    gender = "male"
    name = "Kevin"

    def first_turn(self):
        return "cooperate"

    def take_turn(self, data=()):

        #create list of opponent's last two moves
        last_two_opponent_moves = [data[-1][1], data[-2][1]]
        #if opponent has defected twice, defect, otherwise cooperate
        if "cooperate" not in last_two_opponent_moves:
            return "compete"
        else:
            return "cooperate"