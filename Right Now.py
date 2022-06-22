
from time import sleep
from multiprocessing.sharedctypes import Value

print("\n")

# NOTES: Line to open/read file containing lyrics
Lyrics_file = open("Right Now Lyrics.txt")

# NOTES: .readlines() method used to read each line
lines = Lyrics_file.readlines()
for line in lines:
    sleep(1)
    print(line)


print("\n")

Lyrics_file.close()



