from random import randint
from game_manager import GameManager


class PrimeGame(GameManager):

    def __init__(self):
        super().__init__()
        self.rules = 'Answer "yes" if given number is prime.'\
            'Otherwise answer "no".'

    def generate_question(self):
        self.question = randint(1, 99)
        self.right_answer = 'yes'
        for i in range(2, (self.question // 2) + 1):
            if self.question % i == 0:
                self.right_answer = 'no'
                break

    def make_game(self):
        self.greet()
        print(self.rules)
        while self.round_number <= 2:
            self.round_number += 1
            self.generate_question()
            self.make_round()
            if self.check_answer_result is False:
                break
