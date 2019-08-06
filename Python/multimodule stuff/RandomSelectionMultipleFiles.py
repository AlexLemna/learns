import os
import random
import sys

os.chdir(os.path.dirname(sys.argv[0]))

files = [ 'Data.txt', 'OTHERDATA.txt' ]

def ReadFilesIntoLists ( *TargetFile ):
    for EachFile in TargetFile:
        with open (EachFile, 'r') as file_contents:
            *ListFromFile = file_contents.readlines()

ReadFilesIntoLists ( files )


print()
print (BigList)
print()

BigList = [item.rstrip() for item in BigList]

print()
print (BigList)
print()