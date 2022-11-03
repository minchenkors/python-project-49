import sys
sys.path.insert(1, '/home/minchenkors/python-project-49/brain_games')
from even_game import GameManager

my_game = GameManager()

def main():
    my_game.greet()
    while my_game.round_number <= 3:
        my_game.generate_question()
        my_game.ask_question()
        my_game.check_answer()
        if my_game.check_answer_result == False:
            print(f"'{my_game.player_answer}' is wrong answer ;(. Correct answer was '{my_game.right_answer}'.")
            print(f"Let's try again, {my_game.player_name}!")
            break
        else:
            print('Correct!')
            if my_game.round_number == 3:
                print(f'Congratulations, {my_game.player_name}!')
                break


if __name__ == '__main__':
    main()