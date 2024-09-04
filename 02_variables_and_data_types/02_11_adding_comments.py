# Here I demonstrated my knowledge of variables, values, and strings to construct a message containing a quote that stood out to me once I heard it. 
# First, I added two variables with the value of the author's first and last name. Next, I used an f-string to replace each variable as their respective value.
# This is to ensure that the message will display the variable's value once it prints. I also added a ".title()" command to properly capitalize the author's name.

first_name = "steven"
last_name = "courtney"
full_name = f"{first_name} {last_name}"

message = f'{full_name.title()} once said, "Nothing changes if nothing changes"'
print(message)

# In this second program I practiced the different ways to change the case of a word in string. First, I added a variable containing my name as it's value.
# Then, I used three types of methods used in python that can change the value to all uppercase, lowercase, and title case. 

name = "heidy navarrete-vidals"
print(name.upper())
print(name.lower())
print(name.title())