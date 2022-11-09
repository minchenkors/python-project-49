from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. '\
              'Otherwise answer "no".'


def generate_question():
    question = randint(1, 99)
    answer = 'yes'
    for i in range(2, (question // 2) + 1):
        if question % i == 0:
            answer = 'no'
            break
    return question, answer
