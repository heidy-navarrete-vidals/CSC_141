from random import choice

numbers = ['1', '2', '3', '4', '5',
            '6', '7', '8', '9', '10',
            'a', 'b', 'c', 'd', 'e']

my_ticket = choice(numbers)

for i in range(0, len(numbers)):
    print(choice(numbers))
    if numbers[i] == my_ticket:
        print(f"It took {i+1} times to get the ticket {numbers[i]}")
        break