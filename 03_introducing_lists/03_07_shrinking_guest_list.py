guests = ["cory williams", "jennifer lawrence", "josh hutcherson", "scott cawthon", "matthew lillard", "olivia rodrigo"]
popped = ["cory williams", "jennifer lawrence", "josh hutcherson", "scott cawthon"]

print("I can only invite two people for dinner.")
first_popped = guests.pop(0)
second_popped = guests.pop(0)
third_popped = guests.pop(0)
fourth_popped = guests.pop(0)
for pop in popped:
    print(f"Sorry, {pop.title()}!")

for guest in guests:
    print(f"You are still invited, {guest.title()}!")

del guests[0]
del guests[0]

print(f"This is the deleted list: {guests}")