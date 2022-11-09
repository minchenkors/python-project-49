from random import randint, choice
import operator

DESCRIPTION = 'What is the result of the expression?'
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def generate_question():
    first_number = randint(1, 20)
    second_number = randint(1, 20)
    operator = choice(['+', '-', '*'])
    question = f'{first_number} {operator} {second_number}'
    answer = str(operators[operator](first_number, second_number))
    return question, answer
