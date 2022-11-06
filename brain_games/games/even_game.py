from random import randint

RULES = 'Answer "yes" if the number is even, '\
        'otherwise answer "no".'


def generate_question():
    question = randint(1, 99)
    if question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return {'question': question, 'right_answer': right_answer}
