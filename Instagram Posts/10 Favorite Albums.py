# Lyrically Tech's 10 Favorite Hip-Hop Albums/Projects

from time import sleep
from multiprocessing.sharedctypes import Value

# First step we create a "dictionary" to store the list of albums
# Left of semi-colon (key) is our album and to the right the artist (value)
favorite_hiphop_albums = {
    "Nothing Was The Same" : "Drake",
    "Friday Night Lights" : "J. Cole",
    "Lupe Fiasco's Food & Liquor" : "Lupe Fiasco",
    "The College Dropout" : "Ye",
    "It Was Written": "Nas", 
    "Midnight Marauders" : "A Tribe Called Quest",
    "Purple Haze" : "Cam'ron",
    "American Gangster" : "Jay-Z",
    "The Rising Tied" : "Fort Minor",
    "The Score" : "Fugees"
    }

# Line 23: The beginning of our actual code that outputs to the screen:
print("\n" "Lyrically Tech's 10 Favorite Hip-Hop Projects: ""\n")
for album, artist in favorite_hiphop_albums.items():
    # Delay each album line printed by 1 second:
    sleep(1)
    print("- {} by {}".format(album, artist))
print("\n")
sleep(1)
print("Drop yours below in the comments!")
print("\n")