from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TRCK, TALB, TYER

def edit_metadata(file_path, title, artist, album, year, track):
    # Load the file
    audio = MP3(file_path, ID3=ID3)

    # Add ID3 tag if it does not exist
    if audio.tags is None:
        audio.add_tags()

    # Modify the metadata
    audio.tags["TIT2"] = TIT2(encoding=3, text=title)  # Track title
    audio.tags["TPE1"] = TPE1(encoding=3, text=artist) # Artist
    audio.tags["TALB"] = TALB(encoding=3, text=album)  # Album
    audio.tags["TYER"] = TYER(encoding=3, text=year)   # Year
    audio.tags["TRCK"] = TRCK(encoding=3, text=track)  # Track number

    # Save the changes
    audio.save()
    print("Metadata updated successfully.")

# Example usage
file_path = input('example.mp3')
edit_metadata(file_path, 'New Title', 'New Artist', 'New Album', '2021', '01')

