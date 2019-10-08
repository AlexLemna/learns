from dataclasses import dataclass


@dataclass
class CartesianCoordinate:
    name: str
    x: float = 0.0
    y: float = 0.0


class Thing:
    """A thing that can move."""
