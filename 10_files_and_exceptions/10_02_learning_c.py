# 1/10 difficulty level since it's a small written program.

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text().replace('python', 'C')
print(contents)