#!/usr/bin/env python3
import sys
sys.path.insert(1, '/home/minchenkors/python-project-49/brain_games/games')
from prime_game import PrimeGame  # noqa: E402


def main():
    my_game = PrimeGame()
    my_game.make_game()


if __name__ == '__main__':
    main()
