usernames = ['admin', 'kyle', 'sherman', 'gerard', 'brenda']
for usernames in usernames:
    if usernames == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {usernames.title()}, thank you for logging in again.")