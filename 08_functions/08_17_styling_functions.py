# Function 1:
def make_album(
        artist_name,
        album_title,
        song_number=None):
    """Return dictionary information about an album."""
    album = {'artist': artist_name, 'album': album_title}
    if song_number:
        album['song_number'] = song_number
    return album

#Function 2:
def make_shirt(text = 'I love Python', size='Large'):
    """Display information about a shirt."""
    print(f"\nMake a {size} shirt.")
    print(f"\nAdd the message '{text}' on the shirt.")

#Function 3:
def make_car(
        model,
        manufacturer,
        **car_info):
    """Print information about a car."""
    car_info['model'] = model
    car_info['manufacturer'] = manufacturer
    return car_info