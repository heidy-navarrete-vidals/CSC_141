class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and attributes."""
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restuarant(self):
        """Describe the restaurant."""
        print(f"\nThe name of the restaurant is {self.name}.")
        print(f"The cuisine is {self.cuisine}.")

    def set_number_served(self):
        """"Print the number of customers served."""
        print(f"\nThis restaurant has served {self.number_served} people.")

    def increment_number_served(self, served):
        """Increment number served."""
        self.number_served += served

my_restaurant = Restaurant('Jumbo', 'Chinese')
your_restaurant = Restaurant('Tonis', 'Italian')
his_restaruant = Restaurant('Mikes', 'American')

my_restaurant.set_number_served()

your_restaurant.number_served = 24
your_restaurant.set_number_served()

his_restaruant.increment_number_served(70)
his_restaruant.set_number_served()