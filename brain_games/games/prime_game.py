from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. '\
              'Otherwise answer "no".'


def generate_question_and_answer():
    question = randint(1, 99)
    answer = 'yes'
    if question == 1:
        answer = 'no'
    else:
        for i in range(2, (question // 2) + 1):
            if question % i == 0:
                answer = 'no'
                break
    return question, answer
