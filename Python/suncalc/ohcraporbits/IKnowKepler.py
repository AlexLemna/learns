# For this fantasy planet, the following is "hard canon".
#   * Orbital period = exactly 365 days
#   * The planet reaches periapsis at 00:00am Jan 1 each year
#       (which I *think automatically means...)
#       --> Argument of Periapsis = 270 degrees (it reaches periapsis at the southernmost point from the plane of reference)
#       (and possibly...?)
#       --> Longitide of the Ascending Node (the point where it crosses the reference plane going "upward or "northward")
#   
# The following is "firm canon", meaning it's a working assumption that may change if there's a conflict among hard canon facts. When a value is derived from the others, it is indented and indicated by an arrow.
#   * Planetary mass = Earth's mass = 5.9722x10^24 kilograms = 5972200000000000000000000 kilograms
#   * Stellar standard gravitational parameter = Sun's mass = 1.32712440018x10^20 m^3s^-2 = 132712440018000000000 weird units
#       --> Planetary semimajor axis = 149539307 km
#
#   * Inclination of planetary orbit: -4.5 degrees
#
#   * Planetary eccentricity is 0.0
#       (+ the semimajor axis:)
#       --> Planetary apoapsis (farthest from the sun)
#       --> Planetary periapsis (closest to the sun)
ECCENTRICITY = 0.032
sm_axis = 149539307  # in km
inclination = -4.5  # degrees
peri_arg = 270  # degrees
long_asc_node = 0  # degrees
print()
print ("Calculating apsides... ")
apoapsis = sm_axis * (1 + ECCENTRICITY)
periapsis = sm_axis * (1 - ECCENTRICITY)
print ("The Keplerian elements of the planet's orbit (from a heliocentric reference point) are:")
print (f"   Eccentricity: {ECCENTRICITY}")
print (f"   Semimajor axis: {sm_axis} kilometers")
print (f"       Apoapsis: {apoapsis} kilometers")
print (f"       Periapsis: {periapsis} kilometers")
print (f"   Inclination: {inclination} degrees")
print (f"   Longitude of ascending note: {long_asc_node} degrees")
print (f"   Argument of periapsis: {peri_arg} degrees")
print (f"   If we have a specific date in mind, we can calculate the true anomaly, or the mean anomaly, etc.")

#
# Eccentricity
#   - Periapsis
#   - Apoapsis
# Semimajor axis
#   - Periapsis
#   - Apoapsis
# Inclination just exists
#
# Arg of periapsis = 270
#
# Long of Asc
#   - 
#
# Mean motion (in radians)
#   = squareroot of (gravitational constant[Mass of central object + Mass of orbiting object]/cube of the length of the semimajor asis)