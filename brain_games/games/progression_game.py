from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_question():
    progression_length = randint(5, 10)
    missing_number_position = randint(0, progression_length - 1)
    starting_number = randint(1, 50)
    step = randint(5, 20)
    progression = [
        starting_number + step * i
        for i in range(0, progression_length)
    ]
    right_answer = str(progression[missing_number_position])
    progression[missing_number_position] = '..'
    question = " ".join(map(str, progression))
    return question, right_answer
