#!/usr/bin/env python3
import sys
sys.path.insert(1, '/home/minchenkors/python-project-49/brain_games/games')
from game_manager import GameManager  # noqa: E402


def main():
    my_game = GameManager()
    my_game.greet()


if __name__ == '__main__':
    main()
