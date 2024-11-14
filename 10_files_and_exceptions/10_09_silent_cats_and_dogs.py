# 1/10 difficulty because I only changed one thing.

from pathlib import Path
file_names = ['cats.txt', 'dogs.txt']

for file_name in file_names:
    print(f"\nReading file: {file_name}")

    path = Path(file_name)

    try:
        contents = path.read_text()

    except FileNotFoundError:
        pass

    else:
        print(contents)