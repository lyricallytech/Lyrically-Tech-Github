# Track: Ride Til I Die
# Artist: $ohai

# STEP 1: Import "time", "sleep", and "colorama" modules  
from calendar import TUESDAY
from time import sleep
from multiprocessing.sharedctypes import Value
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init()

print("\n")
print("\n")

# # STEP 2: Retrieve the lyrics from .txt file in the same folder
with open('Ride_Til_I_Die_Text.txt','r') as track:
   
    # For-loop to iterate through each line    
    for line in track:

        # For-loop to iterate through each word
        for word in line.split():
            sleep(1)
            # Print the words           
            print('\033[0;34m' + word)

# Function to print an ellipsis
sleep(1)
def ellipsis(text):
    for periods in text:
        print(periods, end=''),
        sys.stdout.flush()
        sleep(1)


ellipsis('...')
print("\n")
print("\n")

