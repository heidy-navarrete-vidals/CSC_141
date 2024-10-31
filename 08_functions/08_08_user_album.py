def make_album(artist, title):
    """Return information about an album."""
    album = {'artist': artist, 'title': title}
    return album

while True:
    print("\nPlease tell me information about an album:")
    print("(Press 'q' at anytime to quit.)")

    a_name = input("Artist's Name: ")
    if a_name == 'q':
        break
    
    t_name = input("Album Title: ")
    if t_name == 'q':
        break

    album_info = make_album(a_name, t_name)
    print(album_info)