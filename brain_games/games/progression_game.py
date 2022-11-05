from random import randint
from game_manager import GameManager


class ProgressionGame(GameManager):

    def __init__(self):
        super().__init__()
        self.rules = 'What number is missing in the progression?'

    def generate_question(self):
        progression_length = randint(5, 10)
        missing_number_position = randint(0, progression_length - 1)
        starting_number = randint(1, 50)
        step = randint(5, 20)
        progression = [
            starting_number + step * i
            for i in range(0, progression_length)
            ]
        self.right_answer = str(progression[missing_number_position])
        progression[missing_number_position] = '..'
        self.question = " ".join(map(str, progression))

    def make_game(self):
        self.greet()
        print(self.rules)
        while self.round_number <= 2:
            self.round_number += 1
            self.generate_question()
            self.make_round()
            if self.check_answer_result is False:
                break
