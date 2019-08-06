import sys

from main import MainFile


def startfunc():
    _see_me_run = True
    while _see_me_run is True:
        MainFile.mainfunc()
    else:
        sys.exit(1)

startfunc()
