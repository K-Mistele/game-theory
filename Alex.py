from classes.transition_matrix import transition_matrix
class Alex():

    behavior_string = "Does not cooperate; very competitive."
    gender = "male"
    name = "Alex"
    matrix = transition_matrix(((0,1),(0,1)))

    def first_turn(self):
        return "compete"

    def take_turn(self, data=()):
        self.matrix.get_decision(data)
