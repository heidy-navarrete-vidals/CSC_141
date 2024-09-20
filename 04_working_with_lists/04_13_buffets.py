foods = ("egg", "bacon", "waffles", "sausage", "pancakes")

# using a for loop to print each food:

for food in foods:
    print(food)

# this is what it looks like with an intentional error from trying to modify a tuple:
# foods[0] = "hash browns"
# This would cause an error because we cannot assign a new value to an item in tuple

# revised menu

foods = ("egg", "hash browns", "cookies", "waffles", "sausage")
print("\nHere is the revised menu:")
for food in foods:
    print(food)