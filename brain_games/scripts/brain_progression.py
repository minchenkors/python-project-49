#!/usr/bin/env python3
import sys
sys.path.insert(1, '/home/minchenkors/python-project-49/brain_games/games')
from progression_game import ProgressionGame  # noqa: E402


def main():
    my_game = ProgressionGame()
    my_game.make_game()


if __name__ == '__main__':
    main()
