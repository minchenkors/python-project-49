#!/usr/bin/env python3
import sys
sys.path.insert(1, '/home/minchenkors/python-project-49/brain_games/games')
from gcd_game import GCDGame


def main():
    my_game = GCDGame()
    my_game.make_game()


if __name__ == '__main__':
    main()
