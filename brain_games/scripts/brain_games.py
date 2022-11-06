#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(sys.path[0], '../games'))
from game_manager import greet  # noqa: E402


def main():
    greet()


if __name__ == '__main__':
    main()
