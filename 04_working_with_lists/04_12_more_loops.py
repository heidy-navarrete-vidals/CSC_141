# Using first version of 'foods.py' for 04_12_more_loops

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("My favorite foods are:")
for m in my_foods[:3]:
    print(m)

print("My friend's favorite foods are:")
for f in friends_foods[:3]:
    print(f)