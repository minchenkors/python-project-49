from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'


def generate_question():
    first_number = randint(1, 20)
    second_number = randint(1, 20)
    operator = choice(['+', '-', '*'])
    question = f'{first_number} {operator} {second_number}'
    right_answer = str(eval(question))
    return question, right_answer
