from random import choice

my_ticket = ['1', '2', '3', '4', '5',
             '6', '7', '8', '9', '10',
             'a', 'b', 'c', 'd', 'e']

print("Any ticket matching this combination has won:")
for t in range(0,4):
    print(choice(my_ticket))