# 4/10 difficulty because I forgot how for loops work. 

from pathlib import Path
file_names = ['cats.txt', 'dogs.txt']

for file_name in file_names:
    print(f"\nReading file: {file_name}")

    path = Path(file_name)

    try:
        contents = path.read_text()

    except FileNotFoundError:
        print("Cannot find file!")

    else:
        print(contents)