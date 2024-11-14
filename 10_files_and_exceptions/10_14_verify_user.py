# 7/10 difficulty since I'm still not use to classes.

from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        None

def get_new_username(path):
    """Create a new username."""
    username = input("What is your username? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet user."""
    path = Path('username.txt')
    username = get_stored_username(path)
    if username:
        correct = input(f"Is '{username}' your username? (y/n) ")
        if correct == 'y':
            print(f"Welcome back {username}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you next time, {username}")
    else:
        username = get_new_username(path)
        print(f"We'll remember you next time, {username}")

greet_user()
