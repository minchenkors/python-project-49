#!/usr/bin/env python3
import sys
import prompt
sys.path.insert(1, '/home/minchenkors/python-project-49/brain_games/games')


def main():
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')


if __name__ == '__main__':
    main()
