from game_manager import GameManager
from random import randint, choice


class CalcGame(GameManager):

    def __init__(self):
        super().__init__()
        self.first_number = None
        self.second_number = None
        self.operator = None

    def generate_question(self):
        self.first_number = randint(1, 20)
        self.second_number = randint(1, 20)
        self.operator = choice(['+', '-', '*'])
        self.question = f'{self.first_number} {self.operator} {self.second_number}'
        self.right_answer = str(eval(self.question))
    
    def make_game(self):
        self.greet()
        while self.round_number <= 2:
            self.round_number += 1
            self.generate_question()
            self.make_round()
            if self.check_answer_result == False:
                break
            



