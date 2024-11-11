class User:
    """Create a profile of a user."""

    def __init__(self, first_name, last_name, college, age):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.college = college
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Summarize user profiles."""
        print(f"\nThe user's name is {self.first_name} {self.last_name}.")
        print(f"The user is {self.age} and goes to {self.college}.")

    def greet_users(self):
        """Greet users."""
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        """Increment login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts."""
        self.login_attempts = 0

user = User('Michael', 'Myers', 'Haddonfield University','42')

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login attempts(reset): {user.login_attempts}")