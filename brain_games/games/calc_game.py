from random import randint, choice
import operator

DESCRIPTION = 'What is the result of the expression?'
ALLOWED_OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def generate_question_and_answer():
    first_number = randint(1, 20)
    second_number = randint(1, 20)
    operator = choice(list(ALLOWED_OPERATORS.keys()))
    question = f'{first_number} {operator} {second_number}'
    answer = str(ALLOWED_OPERATORS[operator](first_number, second_number))
    return question, answer
