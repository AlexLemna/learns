# --------------------
# RandomSelectionFromFile-multi.py
# --------------------
# Will randomly select one or more items from a local text file and display those items on screen. User will choose how many items it randomly selects.

# *** SOME SETUP STUFF ***
# MODULES FROM PYTHON'S STANDARD LIBRARY
import os # For working within the filesystem
import random # For making random selections. By default, it seeds itself from the current system time.
import sys # So we can use argv[0]

# *** MAIN PROGRAM STARTS HERE ***
loopMain = True
while loopMain is True:
    print()
    userInput = input ( "Enter the desired number of random selections: ")
    try:
        userInteger = int (userInput)
        loopMain = False
    except TypeError:
        print ("We couldn't convert your entry to an integer. Please try again.")
    except:
        print ("Something went wrong. Please try again.")

print ()
print ("PLACEHOLDER TEXT: Input was sucessfully converted to integer.")
print ()

os.chdir(os.path.dirname(sys.argv[0])) # Sets home folder as current working directory, so the file knows where to look for Data.txt

with open('Data.txt', 'r') as fileData:
    fileData = fileData.readlines()
    fileData = [item.rstrip() for item in fileData]
    randomSelections = random.choices ( fileData, k= userInteger )

print ( '\n'.join(randomSelections) ) # prints the list "randomSelections" as a series of entries followed by newlines
