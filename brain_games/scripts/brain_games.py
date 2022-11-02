#!/usr/bin/env python3
import sys
from cli import welcome_user

sys.path.insert(1, '/home/minchenkors/python-project-49/brain_games')


def main():
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
