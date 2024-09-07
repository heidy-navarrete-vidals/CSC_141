guests = ["michael jackson", "jennifer lawrence", "josh hutcherson"]
guests[0] = 'cory williams'
print("Unfortunately, Michael Jackson could not attend.")
for guest in guests:
    print(f"Welcome to dinner, {guest.title()}!")