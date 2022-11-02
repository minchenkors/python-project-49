#!/usr/bin/env python3
import sys
sys.path.insert(1, '/home/minchenkors/python-project-49/brain_games')

from cli import welcome_user

def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    
if __name__ == '__main__':
    main()
