amount = input("How many people are in your dinner group?: ")
amount = int(amount)

if amount >= 8:
    print("\nYou will have to wait for a table.")
else:
    print("\nYour table is ready!")