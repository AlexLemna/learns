from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt


@dataclass
class LatLongPosition:
    name: str
    longitude: float = 0.0
    latitude: float = 0.0

    def distance_to(self, other):
        r = 6_371.007  # Earth radius in km (mean radius)
        λ1, λ2 = radians(self.longitude), radians(other.longitude)
        φ1, φ2 = radians(self.latitude), radians(other.latitude)
        h = (sin (φ2 - φ1) / 2) ** 2 + cos(φ1) * cos(φ2) * sin((λ2 - λ1) / 2) ** 2
        return 2 * r * asin(sqrt(h))

if __name__ == "__main__":
    oslo = LatLongPosition("Oslo", 10.8, 59.9)
    vancouver = LatLongPosition("Vancouver", -123.1, 49.3)
    print (oslo.distance_to(vancouver))
