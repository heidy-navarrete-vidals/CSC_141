def make_album(artist_name, album_title, song_number=None):
    """Return dictionary information about an album."""
    album = {'artist': artist_name, 'album': album_title}
    if song_number:
        album['song_number'] = song_number
    return album

musician_1 = make_album('Tyler the Creator', 'IGOR', song_number=12)
musician_2 = make_album('Mitski', 'Puberty 2')
musician_3 = make_album('Jack Stauber', 'Pop Food')

print(musician_1)
print(musician_2)
print(musician_3)