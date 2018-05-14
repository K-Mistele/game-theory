from classes.transition_matrix import transition_matrix
class Steve:

    behavior_string = "Tit-for-Tat AI. In memoriam Steve Jobs."
    gender = "male"
    name = "Steve"
    matrix = transition_matrix(((1,0), (0,1)))

    def first_turn(self):
        return "cooperate"

    def take_turn(self, data=()):
        self.matrix.get_decision((data))
