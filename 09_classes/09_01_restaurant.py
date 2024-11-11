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

my_restaurant = Restaurant("Chili's", "Mexican")

my_restaurant.describe_restuarant()
my_restaurant.open_restaurant()