#!/usr/bin/env python3
import sys
sys.path.insert(1, '/home/minchenkors/python-project-49/brain_games/games')
import even_game  # noqa: E402
import game_manager  # noqa: E402


def main():
    game_manager.play_game(
        generate_question=even_game.generate_question,
        rules=even_game.RULES
        )


if __name__ == '__main__':
    main()
