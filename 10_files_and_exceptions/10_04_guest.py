# 1/10 difficulty level since it's a small written program.

from pathlib import Path

path = Path('guest.txt')

name = input('What is your name: ')

path.write_text(f"{name}")