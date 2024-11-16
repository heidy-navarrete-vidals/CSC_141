class Employee:
    """A simple class to represent an employee."""

    def __init__(self, f_name, l_name, salary):
        """Initializing attributes."""
        self.first = f_name
        self.last = l_name
        self.salary = salary
    
    def give_raise(self, amount=5000):
        """Give raise to employee."""
        self.salary += amount