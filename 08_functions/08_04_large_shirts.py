def make_shirt(text = 'I love Python', size='Large'):
    """Display information about a shirt."""
    print(f"\nMake a {size} shirt.")
    print(f"\nAdd the message '{text}' on the shirt.")

make_shirt()
make_shirt(size = 'Medium')
make_shirt(text = 'I hate Python', size='Small')