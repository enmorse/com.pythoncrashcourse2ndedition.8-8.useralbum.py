def make_album(artists_name, album_title,
               no_of_songs=None):
    name_and_title = f"{artists_name} {album_title} " \
                     f"{int(no_of_songs)}"
    album = {name_and_title.title()}
    return album


while True:
    print("\nPlease enter the name of your favorite "
          "\nband, the title of one of your favorite "
          "\nalbum created by that band, and the number"
          "\nof songs produced on that title: ")
    print("(Enter 'q' to exit the program)")

    band_name = input("Band Name: ")
    if band_name == 'q':
        break

    album_name = input("Album Name: ")
    if album_name == 'q':
        break

    number_of_songs = input("How Many Songs Are "
                            "On That Album?: ")
    if number_of_songs == 'q':
        break

    album_one = make_album(band_name, album_name, number_of_songs)

    print(f"{album_one} cool band, nice album!")
