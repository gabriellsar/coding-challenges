from math import sqrt
from pygame import draw, Surface


class Planet:
    GRAVITATIONAL_CONSTANT = 6.67

    def __init__(self, pos: tuple, radius: int, mass: int):
        self.x, self.y = pos
        self.radius = radius
        self.mass = mass

    def distance(self, other) -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def apply_gravity(self, other) -> float:
        return self.GRAVITATIONAL_CONSTANT * (self.mass * other.mass) / self.distance(other)

    def draw_planet(self, surface: Surface, color: tuple):
        draw.circle(surface, color, (self.x, self.y), self.radius)
