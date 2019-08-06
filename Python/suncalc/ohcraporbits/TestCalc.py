import math
from math import sin, cos, tan, asin, acos, atan
from math import degrees, radians, pi

ADJ_TO_LAST_NORTHERN_SOLSTICE = 0  # In days
ADJ_TO_PERIHELION = 0 # In days
AXIAL_TILT = -27  # In degrees
ECCENTRICITY = 0
LENGTH_OF_YEAR = 365  # In days

OBSERVER_LONGITUDE = 0
OBSERVER_LATITUDE = 0

# Step x: Calculate basics
#   * obliquity of the ecliptic
#
# Step x: Calculate geocentric ecliptic coordinates
#   IF NECESSARY: date and time as fractional value of ordinal day
#   then
#   * mean longitude of the sun (...corrected for the aberration of light?)
#   * mean anomaly of the sun
#   then
#   * ecliptic longitude
#   * ecliptic latitude
#   * distance from planet to Sun
#
# Step x: Convert into geocentric equitorial coordinates
#   * obliquity of the ecliptic
#   then
#   * right ascension
#   * declination
#
#
# Step x: Convert into horizontal coordinate system
#
#

def subsolar_meridian(hour, minute, second):
    """The meridian, measured in degrees west from the prime meridian, currently experiencing solar noon."""
    _fractional_hour = hour + (minute / 60) + (second / (60 * 60))
    _ssm = 360 * (_fractional_hour / 24)
    return _ssm

def sun_declination(moment):
    """Calculate the solar declination IN RADIANS for any given moment."""
    # From here: https://en.wikipedia.org/wiki/Position_of_the_Sun#Declination_of_the_Sun_as_seen_from_Earth
    _part1 = (radians(360)/LENGTH_OF_YEAR) * (moment + ADJ_TO_PERIHELION)
    _part2 = radians(360/pi) * ECCENTRICITY * sin(_part1)
    _part3 = ((radians(360)/LENGTH_OF_YEAR) * (moment + ADJ_TO_LAST_NORTHERN_SOLSTICE)) + _part2
    _part4 = cos(_part3)
    _part9 = sin(radians(AXIAL_TILT)) * _part4
    _value = asin(_part9)
    return _value 

def hour_angle(sundec_rad):
    """Calculate the hour angle of the sun IN RADIANS for any given declination and latitude."""
    obslat_rad = radians(OBSERVER_LATITUDE)
    _part1 = cos(obslat_rad) * cos(sundec_rad)
    _part2 = sin(radians(-0.83)) - (sin(obslat_rad) * sin(sundec_rad))  # The 0.83 constant is because of atmospheric refraction, assuming an Earth-like atmosphere.
    _value = acos (_part2 / _part1)
    return _value

def get_fractionaldate(month, day, hour, minute, second):
    if month == 0:
        _completed_months = 0
    else:
        _completed_months = month - 1
    _completed_days = day - 1
    _ordinal = (_completed_months * 28) + _completed_days + (hour / 24) + (minute / (24 * 60)) + (second / (24 * 60 * 60))
    return _ordinal

def firstmonth_test():
    file = open("firstmonth-test.txt", "w+")
    for day in range (1,18):
        for hour in range (0,24):
            for minute in range (0,60,15):
                month = 0
                d = day
                h = hour
                m = minute
                s = 0
                o = get_fractionaldate(month, d, h, m, s)
                sundec = sun_declination(o)
                sundec_deg = degrees (sundec)
                ssm = subsolar_meridian(h, m, s)
                ha = hour_angle(sundec)
                ha_deg = degrees(ha)
                print (f"Day {d}, hour {h}, minute {m}, second {s}.")
                # print (f"ORDINAL: {o}", end =" ")
                # print (f"SOLAR DECLINATION: {sundec}")
                file.write (f"Day {d}, hour {h}, minute {m}. SOLAR DECLINATION: {sundec_deg} SSM: {ssm} HA: {ha_deg} \n")

if __name__ == "__main__":
    firstmonth_test()
else:
    pass
