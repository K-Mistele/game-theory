from random import randint
class Alice():

    behavior_string = "Totally unpredictable."
    gender = "female"
    name = "Alice"
    random = __import__("random")

    def first_turn(self):
        random_num = self.random.randint(1,2)
        if random_num == 1:
            return "cooperate"
        else:
            return "compete"

    def take_turn(self, data=()):
        random_num = self.random.randint(1,2)
        if random_num == 1:
            return "cooperate"
        else:
            return "compete"



