from game_manager import GameManager
from random import randint, choice


class GCDGame(GameManager):

    def __init__(self):
        super().__init__()
        self.first_number = None
        self.second_number = None
        self.rules = 'Find the greatest common divisor of given numbers.'

    def gcd_euclid(self):
        dividend = max(self.first_number, self.second_number)
        divisor = min(self.first_number, self.second_number)
        remainder = dividend % divisor
        while remainder != 0:
            dividend = divisor
            divisor = remainder
            remainder = dividend % divisor
        self.right_answer = str(divisor)

    def generate_question(self):
        while True:
            self.first_number = randint(1, 20)
            self.second_number = randint(1, 20)
            if self.first_number != self.second_number:
                break
        self.question = f'{self.first_number} {self.second_number}'
        self.gcd_euclid()
    
    def make_game(self):
        self.greet()
        print(self.rules)
        while self.round_number <= 2:
            self.round_number += 1
            self.generate_question()
            self.make_round()
            if self.check_answer_result == False:
                break
            



