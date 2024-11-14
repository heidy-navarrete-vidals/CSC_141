# 1/10 difficulty level since it's a small written program.

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

lines = contents.splitlines()
line_string = ''
for line in lines:
    line_string += line

print(f"\n{line_string}")