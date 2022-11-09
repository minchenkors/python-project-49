#!/usr/bin/env python3
from brain_games.game_manager import run_game
import brain_games.games.progression_game as progression_game


def main():
    run_game(progression_game)


if __name__ == '__main__':
    main()
