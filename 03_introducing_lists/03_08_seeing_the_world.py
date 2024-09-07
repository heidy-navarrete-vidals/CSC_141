places = ["paris", "japan", "italy", "chicago", "mexico"]

# sorted() example
print(f"This is the original list:{places}")
print(f"\nHere is the sorted list:{sorted(places)}")
print(f"\nThis is the original list:{places}")

# reverse sorted() example
print("\nThis is the reverse-sorted list:")
sorted_places = sorted(places, reverse = True)
print(sorted_places)
print(f"\nThis is the original list:{places}")

# reverse() example
print("\nHere is the reverse ordered list:")
places.reverse()
print(places)
print("\nHere it is reversed again:")
places.reverse()
print(places)

# .sort() example
print("\nHere is the 'sort()' list:")
places.sort()
print(places)
print("\nHere is the reverse 'sort()' list:")
places.sort(reverse = True)
print(places)