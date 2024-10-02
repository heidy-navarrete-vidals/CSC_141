poll = ['brenda', 'jen', 'dora', 'phil']
for poll in poll:
    print(f"\nHello {poll.title()}.")
    if poll == 'jen':
        print("Thank you for responding.")
    elif poll == 'phil':
        print("Thank you for responding.")
    else:
        print("I invite you to respond to the poll!")