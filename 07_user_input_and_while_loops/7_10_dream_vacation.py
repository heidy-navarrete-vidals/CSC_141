responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("What place would you travel to? ")

    responses[name] = response

    repeat = input("Would you like someone else to respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n---Polling Results---")
for name, response in responses.items():
    print(f"{name} would like to travel to {response}.")