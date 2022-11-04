from random import randint
import prompt


class GameManager():

    def __init__(self):
        self.player_name = None
        self.round_number = 0
        self.question = None
        self.player_answer = None
        self.right_answer = None
        self.check_answer_result = None

    def greet(self):
        print('Welcome to the Brain Games!')
        self.player_name = prompt.string('May I have your name? ')
        print(f'Hello, {self.player_name}!')
        
    
    def ask_question(self):
        print(f'Question {self.question}: ')
        self.player_answer = prompt.string('Your answer: ')

    def check_answer(self):
        if self.player_answer == self.right_answer:
            self.check_answer_result = True
        else:
            self.check_answer_result = False
    
    def make_round(self):
        self.ask_question()
        self.check_answer()
        if self.check_answer_result == False:
            print(f"'{self.player_answer}' is wrong answer ;(. Correct answer was '{self.right_answer}'.")
            print(f"Let's try again, {self.player_name}!")
        else:
            print('Correct!')
            if self.round_number == 3:
                print(f'Congratulations, {self.player_name}!')
    