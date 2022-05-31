# Lyrically Tech's 10 Favorite Hip-Hop Albums/Projects

# First step we create a "dictionary" to store the list of albums
# Left of semi-colon is our album and to the right the artist
from multiprocessing.sharedctypes import Value

favorite_hiphop_albums = {
    "It Was Written" : "Nas", 
    "Friday Night Lights" : "J. Cole",
    "Lupe Fiasco's Food & Liquor" : "Lupe Fiasco",
    "The College Dropout" : "Ye",
    "American Gangster" : "Jay-Z",
    "Midnight Marauders" : "A Tribe Called Quest",
    "Nothing Was The Same" : "Drake",
    "Purple Haze" : "Cam'ron",
    "The Rising Tied" : "Fort Minor",
    "The Score" : "Fugees"
}

# Our actual code that outputs to the screen will be below:
print("\n")
for album, artist in favorite_hiphop_albums.items():
    print("{} by {}".format(album, artist))
print("\n")
