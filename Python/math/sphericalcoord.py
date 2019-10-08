from dataclasses import dataclass


@dataclass
class Location_SphericalCoordinates:
    """A representation of location in the spherical coordinates system."""
    ρ: float  # rho - radial distance ('upwardness' from center of planet) - must be >= 0
    θel: float  # theta - polar angle ('northing' from the equator) - measured between (-90° and 90°], or (-π and π] radians
    φraz: float  # phi - azimuthal angle ('easting' from the prime meridian) - measured between (-180° and 180°], or (-π and π] radians
    # -- A Note on Uniqueness of Coordinates --
    # If ρ is 0, then both θinc and φraz are arbitrary. This means that all points where ρ is 0 are functionally equivalent to each other.
    # If θ (elevation) is 90° or -90° (directly above or below the center of planet), then φraz is arbitrary. This means that all points with θ equal to -90° or 90° are functionally equivalent to each other if their ρ is the same.
