#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(sys.path[0], '../games'))
from calc_game import generate_question, RULES  # noqa: E402
from game_manager import play_game  # noqa: E402


def main():
    play_game(
        generate_question=generate_question,
        rules=RULES
        )


if __name__ == '__main__':
    main()
