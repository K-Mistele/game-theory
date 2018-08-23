class Grimm:

    behavior_string = "Cooperates until opponent defects, thereafter always defects (trigger-type AI)"
    gender = "male"
    name = "Grimm"


    def first_turn(self):
        return "cooperate"

    def take_turn(self, data=()):
        if ["cooperate", "compete"] in data or ["compete", "compete"] in data:
            return "compete"
        else:
            return "cooperate"
