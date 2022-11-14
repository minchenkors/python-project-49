from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. '\
              'Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False
    else:
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                return False
    return True


def generate_question_and_answer():
    question = randint(1, 99)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
