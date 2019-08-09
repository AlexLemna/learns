import math
from math import sin, cos, tan, asin, acos, atan
from math import degrees

AXIAL_TILT = None

def arcminutes2degrees(arcminutes):
    _degrees = (arcminutes/60)
    return _degrees

def arcseconds2degrees(arcseconds):
    _degrees = (arcseconds/3600)
    return _degrees

# In degrees
ZENITH_OFFICIAL = 90 + arcminutes2degrees(50)
ZENITH_CIVIL = 96
ZENITH_NAUTICAL = 102
ZENITH_ASTRONOMICAL = 108

class SunlightCalcFormula():
    """An attempt to model equations related to calculating sunrise and setset times."""
    # Using steps from here: https://edwilliams.org/sunrise_sunset_algorithm.htm
    # --------------------
    # Step 1: Get the numerical day of the year. (See the "__init__" section.)
    def __init__(self, yearday, latitude, longitude, rise_or_set):
        self.yearday = yearday
        self.latitude = latitude
        self.longitude = longitude
        self.rise_or_set = rise_or_set
    
    def Calc (self, zenith_type):
        _day = self.yearday
        _lat = self.latitude
        _long = self.longitude
        _rise_or_set = self.rise_or_set
        if zenith_type == "official":
            _zenith = ZENITH_OFFICIAL
        elif zenith_type == "civil":
            _zenith = ZENITH_CIVIL
        elif zenith_type == "nautical":
            _zenith = ZENITH_NAUTICAL
        elif zenith_type == "astronomical":
            _zenith = ZENITH_ASTRONOMICAL
        else:
            raise ValueError
        # --------------------
        # Step 2: Convert the longitude to hour value and calculate an approximate time.
        longitude_hour = _long / 15
        if _rise_or_set == "rise":
            t_approx = _day + ((6 - longitude_hour) / 24)
        elif _rise_or_set == "set":
            t_approx = _day + ((18 - longitude_hour) / 24)
        else:
            raise ValueError

        # --------------------
        # Step 3: Calculate the Sun's mean anomaly.
        mean_anomaly = (0.9856 * t_approx) - 3.289  # <-- XXX: Where do these values come from?

        # --------------------
        # Step 4: Calculate the Sun's true longitude. (XXX: I don't know what this means.) 
        true_longitude = mean_anomaly + (1.916 * sin(mean_anomaly)) + (0.020 * sin(2 * mean_anomaly)) + 282.634
        # Also, this value potentially needs to be adjusted into the range [0,360) by adding or subtracting 360.
        if true_longitude >= 0 and true_longitude < 360:
            pass
        elif true_longitude >= 360:
            true_longitude = true_longitude - 360
        elif true_longitude < 0:
            true_longitude = true_longitude + 360
        else:
            raise ValueError

        # --------------------
        # Step 5a: Calculate the Sun's right ascension.
        right_asc = atan(0.91764 * tan(true_longitude))
        # This potentially needs to be adjusted into the range [0,360) by adding or subtracting 360.
        if right_asc >= 0 and right_asc < 360:
            pass
        elif right_asc >= 360:
            right_asc = right_asc - 360
        elif right_asc < 0:
            right_asc = right_asc + 360
        else:
            raise ValueError
        # --------------------
        # Step 5b: Right ascension value needs to be in the same quadrant as true_longitude.
        TLquadrant = (true_longitude // 90) * 90
        RAquadrant = (right_asc // 90) * 90
        right_asc = right_asc + (TLquadrant - RAquadrant)
        # --------------------
        # Step 5c: Right ascension value needs to be converted into hours.
        right_asc = right_asc / 15

        # --------------------
        # Step 6: Calculate the Sun's declination.
        sin_dec = 0.39782 * degrees (sin(true_longitude))
        cos_dec = degrees(cos (degrees(asin (degrees(sin(sin_dec))))))

        # --------------------
        # Step 7a: Calculate the Sun's local hour angle.
        cos_H = (degrees(cos(_zenith)) - (sin_dec * degrees(sin(_lat)))) / (cos_dec * degrees(cos(_lat)))
        if cos_H > 1:
            pass  # The sun rever rises on this location (on the specified date)
        elif cos_H < -1:
            pass  # The sun never sets on this location (on the specified date)
        else:
            pass
        # --------------------
        # Step 7b: Finish calculating H and convert into hours
        if _rise_or_set == "rise":
            H = 360 - degrees(acos(cos_H))  # If we want rising time
        elif _rise_or_set == "set":
            H = degrees(acos(cos_H))  # If we want setting time
        else: 
            raise ValueError
        H = H / 15

        # --------------------
        # Step 8: Calculate local mean time of rising or setting
        T = H + right_asc - (0.06571 * t_approx) - 6.622

        # --------------------
        # Step 9: Adjust back to UTC
        UTC = T - longitude_hour
        # This potentially needs to be adjusted into the range [0,24) by adding or subtracting 24.
        if UTC >= 0 and UTC < 24:
            pass
        elif UTC >= 24:
            UTC = UTC - 24
        elif UTC < 0:
            UTC = UTC + 24
        else:
            raise ValueError

        # --------------------
        # Step 10: Convert UTC value into local time
        local_offset = None
        local_time = UTC + local_offset
        return local_time
