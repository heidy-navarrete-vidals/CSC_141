# 5/10 difficulty because I forgot how to use while loops.

from pathlib import Path 
path = Path('guest_book.txt')

print("Enter the names of guests attending.")
print("Type 'q' to exit.")
guest_names = []

while True:
    name = input('What is your name: ')

    if name == 'q':
        break
    else: 
        guest_names.append(name)

file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string)