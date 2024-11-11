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

user_1 = User('Michael', 'Myers', 'Haddonfield University','42')
user_2 = User('Charles', 'Ray', 'Slaughter College', '28')
user_3 = User('James', 'Lee', 'Kutztown University', '24')

user_1.describe_user()
user_1.greet_users()

user_2.describe_user()
user_2.greet_users()

user_3.describe_user()
user_3.greet_users()