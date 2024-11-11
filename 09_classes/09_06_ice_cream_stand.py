class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and attributes."""
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restuarant(self):
        """Describe the restaurant."""
        print(f"The name of the restaurant is {self.name}.")
        print(f"The cuisine is {self.cuisine}.")

    def open_restaurant(self):
        """Open restaurant."""
        print(f"{self.name} is now open!")

class IceCreamStand(Restaurant):
    """A simple attempt at modeling an ice cream stand."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize parent and subclass attributes."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = 12
    
    def display_flavors(self):
        """Summarize all the available flavors."""
        print(f"We currently have {self.flavors}!")

my_stand = IceCreamStand('Charlie Icicles', 'Mexican')
my_stand.describe_restuarant()
my_stand.display_flavors()