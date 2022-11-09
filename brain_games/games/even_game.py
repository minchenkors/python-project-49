from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, '\
              'otherwise answer "no".'


def generate_question():
    question = randint(1, 99)
    right_answer = 'yes' if question % 2 == 0 else 'no'
    return question, right_answer
