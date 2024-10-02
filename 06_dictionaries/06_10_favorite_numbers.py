favorite_numbers = {'brenda': ['9', '25'],
                    'dora': ['22', '16'],
                    'jack': ['96', '21'],
                    'tori': ['8', '64'],
                    'matt': ['11', '22']
                    }
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")