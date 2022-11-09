#!/usr/bin/env python3
from brain_games.game_manager import run_game
import brain_games.games.calc_game as calc_game


def main():
    run_game(calc_game)


if __name__ == '__main__':
    main()
