import prompt

GAME_ROUNDS_COUNT = 3


def greet(description=None):
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    if description is not None:
        print(description)
    return player_name


def ask_question(question):
    print(f'Question: {question}')
    player_answer = prompt.string('Your answer: ')
    return player_answer


def check_answer(player_answer, answer):
    return player_answer == answer


def run_game(game):
    player_name = greet(description=game.DESCRIPTION)
    for _ in range(GAME_ROUNDS_COUNT):
        question_params = game.generate_question()
        player_answer = ask_question(question_params[0])
        check_result = check_answer(
            player_answer, question_params[1]
        )
        if not check_result:
            print("'{0}' is wrong answer ;(. ".format(player_answer),
                  "Correct answer was '{0}'.".format(
                  question_params[1])
                  )
            print(f"Let's try again, {player_name}!")
            return
        else:
            print('Correct!')
    print(f'Congratulations, {player_name}!')
