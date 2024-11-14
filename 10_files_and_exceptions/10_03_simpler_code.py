# 1/10 difficulty level since it's a small written program.

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

line_string = ''
for line in contents.splitlines():
    line_string += line

print(f"\n{line_string}")