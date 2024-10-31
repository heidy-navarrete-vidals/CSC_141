def make_sandwich(*toppings):
    """Print items to make a sandwich."""
    print(f"\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('ham', 'cheese', 'lettuce', 'tomatoes')
make_sandwich('cheese', 'turkey', 'cucumbers')
make_sandwich('onions', 'pickles')