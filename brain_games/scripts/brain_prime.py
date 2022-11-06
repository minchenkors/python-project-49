#!/usr/bin/env python3
from brain_games.games.game_manager import play_game
from brain_games.games.prime_game import generate_question, RULES


def main():
    play_game(
        generate_question=generate_question,
        rules=RULES
    )


if __name__ == '__main__':
    main()
