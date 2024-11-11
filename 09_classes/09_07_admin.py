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

class Admin(User):
    """Add an administrator."""

    def __init__(self, first_name, last_name, college, age, privileges):
        """Initialize parent and subclass attributes."""
        super().__init__(first_name, last_name, college, age)
        self.privileges = privileges
    
    def show_privileges(self):
        """Display Admin privileges."""
        print("Privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Admin('Heidy', 'Navarrete', 'Albright', '19', ['can add post', 'can delete post', 'can ban user'])
admin.describe_user()
admin.show_privileges()