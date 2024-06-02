from random import randint

from p5 import circle, noFill, stroke, dist
from complex import Complex


class Circle(object):
    def __init__(self, x: int, y: int, bend: float):
        self.center = Complex(x, y)
        self.bend = bend
        self.radius = abs(1 / bend)

    def show(self):
        stroke(200)

        noFill()
        circle(self.center.real, self.center.imaginary, self.radius * 2)

    def dist(self, other):
        return dist((self.center.real, self.center.imaginary),( other.center.real, other.center.imaginary))
