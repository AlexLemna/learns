def get_ordinal(month, day, hour, minute, second):
    _completed_months = month - 1
    _completed_days = day - 1
    _ordinal = (_completed_months * 28) + _completed_days + (hour / 24) + (minute / (24 * 60)) + (second / (24 * 60 * 60))
    return _ordinal


if __name__ == "__main__":
    for day in range (1,29):
        for hour in range (0,24):
            for minute in range (0,60):
                for second in range (0,60,15):
                    month = 1
                    d = day
                    h = hour
                    m = minute
                    s = second
                    o = get_ordinal(month, d, h, m, s)
                    print (f"Month {month}, day {d}, hour {h}, minute {m}, second {s}. ", end="")
                    print (f"ORDINAL: {o}")
else:
    pass