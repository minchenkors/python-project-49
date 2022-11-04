from random import randint
from game_manager import GameManager


class EvenGame(GameManager):

    def __init__(self):
        super().__init__()
        self.rules = 'Answer "yes" if the number is even, otherwise answer "no".'

    def generate_question(self):
        self.question = randint(1, 99)
        if self.question % 2 == 0:
            self.right_answer = 'yes'
        else:
            self.right_answer = 'no'
    
    def make_game(self):
        self.greet()
        print(self.rules)
        while self.round_number <= 2:
            self.round_number += 1
            self.generate_question()
            self.make_round()
            if self.check_answer_result == False:
                break






