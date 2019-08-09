import csv
import sys

import core
from menu import mainmenu
import orbit
from orbit import get_orbit, update_ta

get_input = mainmenu()
if get_input is True:
    with open("data.csv", "w") as csvfile:
        writer = csv.writer (csvfile)
        now = core.get_now(formatted=False)
        hour = now[0]
        year = now[1]
        while hour < 8759:  # "For year 0" - basically does only a year's worth of calculations, because anything more is redundant
            now = core.get_now(formatted=False)
            hour = now[1]
            year = now[0]
            update_ta(hour)
            orbit = get_orbit()
            ta: float = orbit[5]
            writer.writerow ([hour, ta])
            core.clock_tick()
else:
    sys.exit()


