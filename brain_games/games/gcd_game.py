from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def gcd_euclid(first_number, second_number):
    dividend = max(first_number, second_number)
    divisor = min(first_number, second_number)
    remainder = dividend % divisor
    while remainder != 0:
        dividend = divisor
        divisor = remainder
        remainder = dividend % divisor
    gcd = str(divisor)
    return gcd


def generate_question():
    while True:
        first_number = randint(1, 20)
        second_number = randint(1, 20)
        if first_number != second_number:
            break
    question = f'{first_number} {second_number}'
    right_answer = gcd_euclid(first_number, second_number)
    return {'question': question, 'right_answer': right_answer}
