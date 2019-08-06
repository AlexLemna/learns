# based off of https://github.com/python/cpython/blob/3.7/Lib/datetime.py

MAXYEAR = 1
MAXYEAR = 99999
MONTHNAME_DEF_FULL = [None, "Firstmonth", "Secondmonth", "Thirdmonth", "Fourthmonth", "Fifthmonth", "Sixthmonth", "Seventhmonth", "Eighthmonth", "Ninemonth", "Tenmonth", "Elevenmonth", "Twelvemonth", "Thirteenmonth"]  # Yes, the month names are supposed to change syntax between months eight and nine.
MONTHNAME_DEF_SHORT = [None, "Fir.", "Sec.", "Thrd.", "For.", "Fif.", "Six.", "Sev.", "Egt.", "Nin.", "Ten.", "Elv.", "Twv.", "Thrt."]
DAYNAME_DEF_FULL = [None, "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
DAYNAME_DEF_SHORT = [None, "Sun.", "Mon.", "Tues.", "Weds.", "Thurs.", "Fri.", "Sat."]


def _compare(x, y):
    if x == y:
        return 0
    elif x > y:
        return 1
    elif x < y:
        return -1
    else:
        raise TypeError("Something impossible happened. See the '_compare' function.")


# SO... THIS NEXT SECTION REQUIRES SOME EXPLANATION.
# Look the following function over. If you have questions, a detailed explanation is at the end of this function.
def fantasydate(day_of_year):
    '''Converts a numerical day of the year to a (month, monthday) tuple.'''
    _MONTH_LENGTH = 28
    _ML = _MONTH_LENGTH
    if type (day_of_year) is str:
        day_of_year = int (day_of_year)
    
    if day_of_year < 1 or day_of_year > 365:
        raise ValueError("'day_of_year' must be equal to or between 1 and 365.")
    elif day_of_year <= 182:
        _month_number = ((day_of_year - 1) // _ML) + 1
        _day_of_month = ((day_of_year - 1) % _ML) + 1  
    elif day_of_year == 183:
        _month_number = 7
        _day_of_month = None  # Midyear's Day, omitted from traditional date count
    elif day_of_year >= 184:
        day_of_year = day_of_year - 1  # Adjustment for Midyear's Day
        _month_number = ((day_of_year - 1) // _ML) + 1
        _day_of_month = ((day_of_year - 1) % _ML) + 1
    else:  # This shouldn't happen.
        raise ValueError(f"The 'day_of_year', {day_of_year}, is invalid.")
    return _month_number, _day_of_month # Returns a tuple
# !!! WIP - Detailed explanation goes here
# The "//" is "truncation division" - it returns an integer.
# The "%" is "modulus" - it returns the remainder.
# "+1" because no month 0
# "+1" because no monthday 0


def main(_user_input):
    if __name__ == "__main__":
        try:
            # Commented out for testing:
            # _user_input = int (input ("What day of the year is it? "))

            # Assign the values of the tuple returned by the function.
            month_number, day_of_month = fantasydate (_user_input)

            if month_number == 7 and day_of_month == None:
                print (f"That means today is Midyear's Day.")
            elif month_number < 1 or month_number > 13 or day_of_month < 1 or day_of_month > 28:
                raise ValueError
            elif day_of_month == 1 or day_of_month == 21:
                print (f"That means today is the {day_of_month}st of {MONTHNAME_DEF_FULL[month_number]}.")
            elif day_of_month == 2 or day_of_month == 22:
                print (f"That means today is the {day_of_month}nd of {MONTHNAME_DEF_FULL[month_number]}.")
            elif day_of_month == 3 or day_of_month == 23:
                print (f"That means today is the {day_of_month}rd of {MONTHNAME_DEF_FULL[month_number]}.")
            else:
                print (f"That means today is the {day_of_month}th of {MONTHNAME_DEF_FULL[month_number]}.")
        except KeyboardInterrupt:
            pass
    else:
        pass

for date in range(1,366):
    main(date)
