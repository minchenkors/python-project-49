from random import randint
import prompt


class GameManager():

    def __init__(self):
        self.player_name = None
        self.round_number = 0
        self.number_for_player = None
        self.player_answer = None
        self.right_answer = None
        self.check_answer_result = None

    def greet(self):
        print('Welcome to the Brain Games!')
        self.player_name = prompt.string('May I have your name? ')
        print(f'Hello, {self.player_name}!')
        print('Answer "yes" if the number is even, otherwise answer "no".')

    def generate_question(self):
        self.number_for_player = randint(1, 99)
        if self.number_for_player % 2 == 0:
            self.right_answer = 'yes'
        else:
            self.right_answer = 'no'
    
    def ask_question(self):
        print(f'Question {self.number_for_player}: ')
        self.player_answer = prompt.string('Your answer: ')

    def check_answer(self):
        if self.player_answer == self.right_answer:
            self.check_answer_result = True
            self.round_number += 1
        else:
            self.check_answer_result = False
    





