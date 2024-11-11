from random import randint

class Die():
    """A simple class representing a dice."""

    def __init__(self, sides=6):
        """Initialize attributes."""
        self.sides = sides

    def roll_die(self):
        """Randomly roll the dice."""
        print(randint(1, self.sides))

first = Die(6)
second = Die(10)
third = Die(20)

print("\nThe 6-sided die:")
for f in range(0, 10):
    first.roll_die()

print("\nThe 10-sided die:")
for s in range(0,10):
    second.roll_die()

print("\nThe 20-sided die:")
for t in range(0,10):
    third.roll_die()