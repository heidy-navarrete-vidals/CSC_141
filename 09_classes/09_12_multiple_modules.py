"""A set of classes used to represent an Admin."""

from user_module import User

class Privileges():
    """List of privileges for Admin."""

    def __init__(self, privileges):
        """Initialize attributes."""
        self.privileges = privileges
    
    def show_privileges(self):
        """Display Admin privileges."""
        print("Privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """Add an administrator."""

    def __init__(self, first_name, last_name, college, age, priveleges):
        """Initialize parent and subclass attributes."""
        super().__init__(first_name, last_name, college, age)
        self.privileges = Privileges(priveleges)

admin = Admin('Heidy', 'Navarrete', 'Albright', '19', ['can ban user', 'can delete post'])
admin.describe_user()
admin.privileges.show_privileges()