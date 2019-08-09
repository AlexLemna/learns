# Initial values
_hour = 0
_year = 0

_now = {
    "hour" : _hour,
    "year" : _year,
}

def clock_tick ():
    h = _now.get ("hour")
    y = _now.get ("year")
    # There are 8,760 hours in a year
    if 0 <= h < 8759:
        _now.update (hour=h+1)
    elif h == 8759:
        _now.update (hour=0)
        _now.update (year=y+1)
    else:
        raise ValueError

def get_now (formatted: bool=True):
    h = _now.get ("hour")
    y = _now.get ("year")
    if formatted is True:
        d, h = divmod (h, 24)
        d = d + 1  # It's Jan 1st, not Jan 0th
        result = (y, d, h)
    elif formatted is False:
        result = (y, h)
    else:
        raise ValueError
    return result
