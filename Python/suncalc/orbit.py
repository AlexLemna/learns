# Constants
_SEMIMAJOR_AXIS = 0  # measured in meters
_ECCENTRICITY = 0  # dimensionless
_INCLINATION = 0  # measured in degrees 0 - 360
_LONGITUDE_OF_THE_ASCENDING_NODE = 0  # measured in degrees 0 - 360
_ARGUMENT_OF_PERICENTER = 0  # measured in degrees 0 - 360
# Initial values
_true_anomaly: float = 0

_orbit = {
    "a" : _SEMIMAJOR_AXIS, 
    "e" : _ECCENTRICITY,  # dimensionless
    "inc" : _INCLINATION,  # measured in degrees 0 - 360
    "asc" : _LONGITUDE_OF_THE_ASCENDING_NODE,  # measured in degrees 0 - 360
    "pr" : _ARGUMENT_OF_PERICENTER,  # measured in degrees 0 - 360
    "ta" : _true_anomaly,  # measured in degrees 0 - 360
}

_TA_DEGREES_PER_HOUR: float = (365/8760)
def update_ta (hours_since_new_year: int):
    current_ta = hours_since_new_year * _TA_DEGREES_PER_HOUR
    _orbit.update (ta=current_ta)

def get_orbit ():
    a= _orbit.get ("a")
    e = _orbit.get ("e")
    inc = _orbit.get ("inc")
    asc = _orbit.get ("asc")
    pr = _orbit.get ("pr")
    ta = _orbit.get ("ta")
    result = (a, e, inc, asc, pr, ta)
    return result
