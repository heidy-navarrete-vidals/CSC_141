#  Accessing Elements in a List, Index Positions Start at 0, Not 1, Using Individual Values from a List
languages = ["spanish", "english", "japanese", "korean"]
print(f"My first language is {languages[1].title()}.")
print(languages[3].title())

# Modifying, Adding, and Removing Elements
print("\n")
cakes = ["strawberry", "chocolate", "vanilla"]
cakes[0] = "carrot"
cakes.append("velvet")
cakes.insert(3, "coffee")
print(cakes)

del cakes[1]
print(cakes)

popped_cake = cakes.pop(3)
print(cakes)

cakes.remove("coffee")
print(cakes)

# Organizing a List
print("\n")
icecreams = ["mint", "chocolate", "strawberry", "cherry"]
print(f"This is the original list: {icecreams}")
print("\nHere is the sort() list:")
icecreams.sort()
print(icecreams)
print("\nHere is the reverse sort() list:")
icecreams.sort(reverse = True)
print(icecreams)

print("\nHere is the sorted list:")
print(sorted(icecreams))
print("\nHere is the reverse sorted list:")
sorted_icecreams = sorted(icecreams, reverse = True)
print(sorted_icecreams)

print("\nHere is the reverse() list:")
icecreams.reverse()
print(icecreams)

print(len(icecreams))