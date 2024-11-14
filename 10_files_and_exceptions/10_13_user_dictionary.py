# 8.5/10 difficulty because it was hard to understand some of the code, I think this is probably the longest program I've coded so it was a total eyestrain.

from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored user info if available."""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        None

def get_new_user_info(path):
    """Get info from new user."""
    username = input("What is your name: ")
    pet = input("What pet do you have: ")
    location = input("Where do you live: ")

    user_dict = {
        'username': username,
        'pet': pet,
        'location': location,
    }
    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict

def greet_user():
    """Greet user by name."""
    path = Path('user_info.json')
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['username']}.")
        print(f"How is your {user_dict['pet']}?")
        print(f"We hope its been great at {user_dict['location']}.")
    else:
        user_dict = get_new_user_info(path)
        msg = f"We'll remember you next time, {user_dict['username']}."
        print(msg)

greet_user()