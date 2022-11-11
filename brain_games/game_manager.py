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


def run_game(game):
    player_name = greet(description=game.DESCRIPTION)
    for _ in range(GAME_ROUNDS_COUNT):
        question, answer = game.generate_question_and_answer()
        player_answer = ask_question(question)
        if player_answer != answer:
            print("'{0}' is wrong answer ;(. ".format(player_answer),
                  "Correct answer was '{0}'.".format(
                  answer)
                  )
            print(f"Let's try again, {player_name}!")
            return
        else:
            print('Correct!')
    print(f'Congratulations, {player_name}!')
