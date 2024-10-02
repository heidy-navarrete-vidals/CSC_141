friend_01 = {'first_name': 'brenda',
             'last_name': 'rico',
             'age': '20',
             'city': 'reading'
             }
friend_02 = {'first_name': 'dora',
            'last_name': 'boteng',
            'age': '18',
            'city': 'reading'
            }
friend_03 = {'first_name': 'meg',
             'last_name': 'thomas',
             'age': '20',
             'city': 'reading'
             }
friends = [friend_01, friend_02, friend_03]
for friend in friends:
    print(f"\n{friend}")
    for key, value in friend.items():
        print(f"\n{key.title()}: {value.title()}")