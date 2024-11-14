# 7/10 difficulty only because I still don't understand the 'encoding='utf-8' part that was used as an example in the book.

from pathlib import Path
path = Path("common_words.txt")


try:
    contents = path.read_text(encoding='utf-8')

except FileNotFoundError:
    print(f"Sorry, filename {path} does not exist.")

else:
    words = contents.lower().count('the ')
    print(words)