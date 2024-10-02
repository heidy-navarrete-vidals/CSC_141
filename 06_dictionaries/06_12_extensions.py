# extended version of 06_01_person.py assignment:

friends = {
    'brenda': {
        'age': '20',
        'pets': 'turtle',
        'loves': 'horror movies',
        'hates': 'chocolate',
    },

    'daniel': {
        'age': '19',
        'pets': 'cat',
        'loves': 'Hollow Knight',
        'hates': 'Dead by Daylight',
    },

    'tori': {
        'age': '19',
        'pets': 'dog',
        'loves': 'Undertale',
        'hates': 'homework',
    },
}

for friend, friend_info in friends.items():
    print(f"\nFriend Name: {friend.title()}")

    age = friend_info['age']
    pets = friend_info['pets']
    loves = friend_info['loves']
    hates = friend_info['hates']

    print(f"\tAge: {age}")
    print(f"\tPets: {pets}")
    print(f"\tLoves: {loves}")
    print(f"\tHates: {hates}")

