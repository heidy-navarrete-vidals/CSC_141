# 1/10 kind of seems like the same exact program as the previous assignment

from pathlib import Path
import json

path = Path('favorite_number.json')


contents = path.read_text()


number = input("What is your favorite number: ")
contents = json.dumps(number)
path.write_text(contents)
print("I will remember that number.")

number = json.loads(contents)
print(f"I have your favorite number. It's {number}!")

