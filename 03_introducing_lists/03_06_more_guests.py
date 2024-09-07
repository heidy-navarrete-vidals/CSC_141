guests = ["michael jackson", "jennifer lawrence", "josh hutcherson"]
guests[0] = 'cory williams'
guests.insert(0, "scott cawthon")
guests.insert(3, "matthew lillard")
guests.append("olivia rodrigo")

print("I have found a bigger table.")
for guest in guests:
    print(f"Welcome to dinner, {guest.title()}!")