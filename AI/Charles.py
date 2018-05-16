class Charles:

    behavior_string = "Ruthlessly exploits friendly AIs"
    gender = "male"
    name = "Charles"

    def first_turn(self):
        return "cooperate" # lull enemy AI into thinking its friendly

    def take_turn(self, data):
        if data[-1][1] == "cooperate": # if enemy AI cooperated last turn
            return "compete"
        else: # if enemy AI competed last turn
            if (len(data) >= 3 and # if at least three items in data list
            # if enemy AI has competed the last three games
            ([data[-1], data[-2], data[-3]].count(["compete", "compete"]) == 3 or
            [data[-1], data[-2], data[-3]].count(["cooperate", "compete"]) == 3)):
                # try cooperating to lure into cooperating
                return "cooperate"
            else:
                return "compete"
