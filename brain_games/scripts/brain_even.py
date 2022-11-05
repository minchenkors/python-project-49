#!/usr/bin/env python3
import sys
sys.path.insert(1, '/home/minchenkors/python-project-49/brain_games/games')
from even_game import EvenGame  # noqa: E402


def main():
    my_game = EvenGame()
    my_game.make_game()


if __name__ == '__main__':
    main()
