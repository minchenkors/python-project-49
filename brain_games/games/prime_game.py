from random import randint

RULES = 'Answer "yes" if given number is prime. '\
        'Otherwise answer "no".'


def generate_question():
    question = randint(1, 99)
    right_answer = 'yes'
    for i in range(2, (question // 2) + 1):
        if question % i == 0:
            right_answer = 'no'
            break
    return {'question': question, 'right_answer': right_answer}
