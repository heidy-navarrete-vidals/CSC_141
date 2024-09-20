# first program modification:

animals = ['cat', 'dog', 'turtle']
for animal in animals:
    print(animal.title())
    print(f"A {animal} would make a great pet!\n")
print("All of these animals have four legs. They would also be great pets!")

# second program modification:

animals = [
    'cat', 'dog', 'turtle',
    'fish', 'hamster', 'parrot',
    'rat', 'snake', 'iguana'
]
print(f"The first three items in the list are:{animals[0:3]}")
print(f"The items from the middle of the list are:{animals[3:6]}")
print(f"The first three items in the list are:{animals[6:9]}\n")

# third program modification:

numbers = []

for i in range(1,1000001):
    numbers.append(i)
print(min(numbers))
print(max(numbers))
print(sum(numbers))