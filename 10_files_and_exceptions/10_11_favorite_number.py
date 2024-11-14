# 6/10 a little confusing overall since the topic is new

from pathlib import Path
import json

answer = input("What is your favorite number: ")

path = Path('number.json')
contents = json.dumps(answer)
path.write_text(contents)
print("I'll remember that number!")

contents = path.read_text()
number = json.loads(contents)
print(f"\nYour favorite number is {number}.")