current_users = ['brenda', 'eren', 'chucky', 'jason', 'michael']
new_users = ['freddy', 'billy', 'afton', 'brenda', 'mike']
for new_users in new_users:
    if new_users in current_users:
        print("You must enter a different username.")
    else:
        print("That username is available!")