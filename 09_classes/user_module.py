# created for 09_12_multiple_modules

"""A class modeling a user profile."""

class User:
    """Create a profile of a user."""

    def __init__(self, first_name, last_name, college, age):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.college = college
        self.age = age

    def describe_user(self):
        """Summarize user profiles."""
        print(f"\nThe user's name is {self.first_name} {self.last_name}.")
        print(f"The user is {self.age} and goes to {self.college}.")
    
    def greet_users(self):
        """Greet users."""
        print(f"Hello, {self.first_name} {self.last_name}!")