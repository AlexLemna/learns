import os
import sys

def main():
    os.chdir (os.path.dirname (sys.argv[0]))
    with open("sampledatafile.txt", "r") as f:
        for line in f.readlines():
            _upperstr = str.upper (line)
            print (_upperstr)

if __name__ == "__main__":
    main()
