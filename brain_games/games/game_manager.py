import prompt


def greet(rules=None):
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    if rules is not None:
        print(rules)
    return player_name


def ask_question(question):
    print(f'Question: {question}')
    player_answer = prompt.string('Your answer: ')
    return player_answer


def check_answer(player_answer, right_answer):
    if player_answer == right_answer:
        return True
    else:
        return False


def play_game(generate_question, rules):
    round_number = 0
    player_name = greet(rules=rules)
    while round_number <= 2:
        round_number += 1
        question_params = generate_question()
        player_answer = ask_question(question_params['question'])
        check_result = check_answer(
            player_answer, question_params['right_answer']
        )
        if check_result is False:
            print("'{0}' is wrong answer ;(. ".format(player_answer),
                  "Correct answer was '{0}'.".format(
                  question_params['right_answer'])
                  )
            print(f"Let's try again, {player_name}!")
            break
        else:
            print('Correct!')
            if round_number == 3:
                print(f'Congratulations, {player_name}!')
